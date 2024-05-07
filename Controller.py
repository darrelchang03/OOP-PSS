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

    def create_task(self, name, task_type, start_time, duration, date):
        try:
            new_task = Task(name, task_type, start_time, duration, date)
            self.model.add_task(new_task)
            self.viewer.display_message("Task added successfully.")
        except ValueError as e:
           self.viewer.display_error(str(e))

    def show_tasks(self):
        for task in self.scheduler.tasks:
            self.viewer.display_task(task)

    def remove_task(self, task):
        try:
            self.model.delete_task(task)
            self.viewer.display_message("Task deleted successfully")
        except ValueError as e:
            self.viewer.diplay_error(str(e))

    def update_name(self, taskName):
        try:
            self.model.update_task_name(taskName)
            self.viewer.display_message(f"Task name {taskName} updated successfully")
        except ValueError as e:
           self.viewer.display_error(str(e))

    # Private methods
