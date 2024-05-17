'''
Handles all user interface logic.
Displays tasks, error messages, and other outputs to the user.
Can be implemented via a simple console interface or a more complex graphical interface, depending on your preference and time constraints.
'''

import Model
import Task
import Viewer
import Controller

class Viewer():

    # Contructor
    '''
    def display_error(self, message):
        print("Error:", message)
    
    def display_message(self, message):
        print(message)
    
    # Other public Methods: Display day, display week, display month
        

    month = 1
    week = 1
    day = 1
    #Starts calendar on first day of first week of month

    #need to figure out parameters later but for now there's presumed parameters on display methods
    def display_month(month):
        print("Month: " + month)
        
    def display_week(week):
        print("Week: " + week)

    def display_day(day):
        print("Day: " + day)
    

    # Private Methods
        #should be something that updates month day and week depending on the controller

    def update_month(newMonth):
        month = newMonth
        
    def update_week(newWeek):
        week = newWeek

    def update_day(newDay):
        day = newDay
    '''

    def __init__(self, model):
        self.model = model

# Added task as parameter. A list of tasks will be given by the controller to display
    def display_tasks(self, tasks):
        if not tasks:
            print("\nNo tasks scheduled.")
            return

        for task in tasks:
            print("Name:", task.name)
            print("Type:", task.type)
            print("Start Time:", task.startDateTime.strftime("%Y-%m-%d %H:%M"))
            print("Duration:", task.duration, "hours")
            print("")

    def prompt_add_task(self):
        # This method should just be prompting the user. And then return the user's inputs
        # it doesnt need to call the model, thats the Controllers job.

        # name, task_type, start_time, duration, date = self.prompt_task_details()
        # task = Task.TransientTask(name, task_type, start_time, duration, date)
        # try:
        #     self.model.add_task(task)
        #     print("Task added successfully.")
        # except ValueError as e:
        #     print(f"Error adding task: {e}")
        print("Creating new task")
     
        return self.prompt_task_details()

    
	

    def prompt_delete_task(self):
        # This method should just be prompting the user. And then return the user's inputs
        # it doesnt need to call the model, thats the Controllers job.
        name = input("Enter the name of the task to delete: ")
        return name
        # task = self.model.task_exists_by_name(name)
        # if task:
        #     try:
        #         self.model.delete_task(task)
        #         print("\nTask deleted successfully!")
        #     except ValueError as e:
        #         print(f"Error deleting task: {e}")
        # else:
        #     print("Task not found!")

    def prompt_task_details(self):
        name = input("Enter task name: ")
        task_type = input("Enter task type: ")
        start_time = float(input("Enter start time (24 hr clock e.g., 7:45 PM == 19.75): "))
        duration = float(input("Enter duration: "))
        date = int(input("Enter date (YYYYMMDD): "))
        return name, task_type, start_time, duration, date
    
    def prompt_view_schedule(self):
        days = input("How many days in advance would you like to view your schedule")
        return days

# This should just return the inputs given by the user
    def menu(self):
#        while True:
#            print("\n------- Task Menu -------")
            print("1. Display Tasks")
            print("2. Add Task")
            print("3. Delete Task")
            print("4. Exit")
            choice = input("Choose choice: ")
            return choice
#            choice = input("Enter a number: ")
#            if choice == '1':
#                self.display_tasks()
#            elif choice == '2':
#                self.add_task()
#            elif choice == '3':
#                self.delete_task()
#           elif choice == '4':
###           else:
 # #             print("Invalid choice. Please try again.")
    


    if __name__ == "__main__":
        model = Model.Model()
        viewer = Viewer(model)
        viewer.menu()
