'''
Acts as an intermediary between the model and view.
Processes user input from the view and updates the model.
Retrieves data from the model to update the view.
'''
import Model
import Task
import Viewer
import Controller

class Controller():
    def __init__(self):
        self.model = Model
        self.viewer = Viewer

    # def create_task(self, name, task_type, date, start_time, duration):
    #   try:
    #
    #   except ValueError as e:
    #       self.view.display_error(str(e))

    # def show_tasks(self):
        # for task in self.scheduler.tasks:
        #     self.view.display_task(task)