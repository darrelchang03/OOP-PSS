'''
Acts as an intermediary between the model and view.
Validates user input from the view and calls method models.
Retrieves data from the model to update the view.
'''
import Model
import Task
import Viewer
import Controller

class Controller():

    # Contructor

    def __init__(self):
        self.model = Model
        self.viewer = Viewer

    # Public methods

    def create_task(self, name, task_type, date, start_time, duration):
        try:
            new_task = Task(name, task_type, date, start_time, duration)
            self.scheduler.add_task(new_task)
            self.view.display_message("Task added successfully.")
        except ValueError as e:
           self.view.display_error(str(e))

    def show_tasks(self):
        for task in self.scheduler.tasks:
            self.view.display_task(task)

    # Private methods