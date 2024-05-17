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

    def __init__(self):
        self.model = Model
        self.viewer = Viewer

    # Public methods

# 
    def create_task(self, name, task_type, start_time, duration, date):
        # call viewer to prompt for task
        # get values returned and validate
        # Validate using model methods
        # If valid create Task and add it to the model
        try:
            new_task = Task(name, task_type, start_time, duration, date)
            self.model.add_task(new_task)
            self.viewer.display_message("Task added successfully.")
        except ValueError as e:
           self.viewer.display_error(str(e))
    
    def create_anti_task(self, task):
        # call viewer to prompt for task
        # get values returned and validate
        # Validate using model methods
        # If valid create Task and add it to the model
        try:
            new_anti_task = Task.AntiTask(self, task)
            self.model.add_anti_task(new_anti_task)
            self.viewer.display_message("AntiTask added successfully.")
        except ValueError as e:
           self.viewer.display_error(str(e))

    def remove_task(self, task):
        # call viewer to prompt for task
        # get values returned and validate
        # Validate using model methods
        # If valid delete using the model methods
        try:
            self.model.delete_task(task)
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
