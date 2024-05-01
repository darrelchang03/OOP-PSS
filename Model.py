'''
Handles the data logic.
Task objects with properties such as name, type, date, start time, duration, etc.
A Scheduler class to manage the collection of tasks, ensuring no overlaps and handling the insertion and deletion of tasks.
'''

import Model
import Task
import Viewer
import Controller

from datetime import datetime, timedelta
class Model():

# Contructor

    def __init__(self):
        # List of task objects
        self.tasks = []

# Public Methods

    def add_task(self, task):
        for existing_task in self.tasks:
            if self.tasks_overlap(task, existing_task):
                raise ValueError('Task overlap with an existing task')
        self.tasks.append(task)

# Private methods
    def __create_datetime(self, date, time):
        year = int(date / 10000)
        month = int(date / 100 % 100)
        day = int(date % 100)
        hours = int(time)
        minutes = (int(time - hours) * 60)
        
        return datetime(year, month, day, hours, minutes)

    def __tasks_overlap(self, task1, task2):
        start1 = self.create_datetime(task1['date'], task1['start_time'])
        end1 = start1 + timedelta(hours=task1['duration'])

        start2 = self.create_datetime(task2['date'], task2['start_time'])
        end2 = start2 + timedelta(hours=task2['duration'])

        return max(start1, start2) < min(end1, end2)