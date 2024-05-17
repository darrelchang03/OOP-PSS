'''
Acts as an intermediary between the model and view.
Validates user input from the view and calls method models.
Retrieves data from the model to update the view.
'''
import Model
import Task
import Viewer

class Controller():

    # Contructor

# Needs to call viewer menu method, take in the inputs and call methods accordingly
    def __init__(self):
        self.model = Model
        self.viewer = Viewer

    # Public methods

# 
    def call_menu(self):
        try:
            output = self.viewer.menu()
            x = True
            while (x):
                if output == '1':
                    self.show_tasks()
                    x = False
                elif output == '2':
                    self.create_task()
                    x = False
                elif output == '3':
                    self.remove_task()
                    x = False
                elif output == '4':
                    self.viewer.display_message("Exiting")
                    x = False
                else:
                    self.viewer.display_message("Invalid choice. Please try again.")
                    output = self.viewer.menu()

        except ValueError as e:
           self.viewer.display_error(str(e))
# 
    def create_task(self):
        try:
            # call viewer to prompt for task
            self.viewer.display_message("Enter your task details:")
            details = self.viewer.prompt_task_details()
            new_task = Task(details)

            # Validate using model methods - no model function exists
            # If valid create Task and add it to the model
            self.model.add_task(new_task)
            self.viewer.display_message("Task added successfully.")
        except ValueError as e:
           self.viewer.display_error(str(e))
    
    def create_anti_task(self):
        try:
            # call viewer to prompt for task
            self.viewer.display_message("Enter your task details:")
            details = self.viewer.prompt_task_details()
            new_task = Task(details)

            # Validate using model methods
            # If valid create Task and add it to the model
            new_anti_task = Task.AntiTask(self, new_task)
            self.model.add_anti_task(new_anti_task)
            self.viewer.display_message("AntiTask added successfully.")
        except ValueError as e:
           self.viewer.display_error(str(e))

    def remove_task(self):
        # call viewer to prompt for task
        # get values returned and validate
        # Validate using model methods
        # If valid delete using the model methods
        try:
            name = self.viewer.prompt_delete_task("Enter your task name:")
            task = self.model.task_exists_by_name(name)
            if(task != False):
                self.model.delete_task(task)
            else:
                self.viewer.display_message("Task does not exist.")
            self.viewer.display_message("Task deleted successfully")
        except ValueError as e:
            self.viewer.diplay_error(str(e))


    def update_name(self):
        # call viewer to prompt for task
        # get values returned and validate
        # Validate using model methods
        # If valid create Task and add it to the model
        taskName = # viewer prompt method
        # call method to see if task exist
        try:
            self.model.update_task_name(taskName)
            self.viewer.display_message(f"Task name {taskName} updated successfully")
        except ValueError as e:
           self.viewer.display_error(str(e))


    def show_tasks(self):
        # call viewer to prompt for days in advance to see schedule
        # get values returned and validate
        # Call model for tasks
        # Call viewer to display the list of tasks
        for task in self.scheduler.tasks:
            self.viewer.display_task(task)

    # Private methods
