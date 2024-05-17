'''
Handles the data logic.
Task objects with properties such as name, type, date, start time, duration, etc.
A Scheduler class to manage the collection of tasks, ensuring no overlaps and handling the insertion and deletion of tasks.
'''

import Model
import Task
import Viewer
import Controller
import json

from datetime import datetime, timedelta
from Task import *

class Model():

# Contructor

    def __init__(self):
        # List of task objects
        self.tasks = []
       

# Public Methods

    def add_task(self, task):
        #checks if the existing task is a recurring task 
        for existing_task in self.tasks:
            if (isinstance(existing_task, RecurringTask)):

                #checks the occurences and sees if the tasks overlap
                for occurence in existing_task.occurences(datetime.today(), existing_task.endDatetime):

                    #if tasks the anti_tasks overlap with the tasks, we can add tasks
                    if self.__tasks_overlap(existing_task, task):
                        
                        for task in self.tasks:
                            if self.__tasks_completely_overlap(task, existing_task) and isinstance(task, AntiTask):
                                self.tasks.append(task)
                                return
                            else:
                                continue
                        else:
                            raise ValueError("No anti task that match")

            elif self.__tasks_overlap(task, existing_task): 
        
                raise ValueError('Task overlaps with an existing task')
            
        else:
            self.tasks.append(task)

    # def add_anti_task(self, task):

    # Returns true if anti_task is added, and specific errors if the anti-task cannot be added
    def add_anti_task(self, anti_task):
       #checks if task is a recurring task and if task is the same duration as anti task
        if isinstance(anti_task, AntiTask):
            for task in self.tasks:
                if (isinstance(task, RecurringTask) and task.duration == anti_task.duration):
                    for occurence in task.occurences(datetime.today(), task.endDatetime):
                        if occurence == anti_task.startDateTime:
                            self.tasks.append(anti_task)
                            return True
            # Went through all the tasks and there was no matching time for recurring tasks
            else:
                raise ValueError('No recurring task found for anti-task')
        else: 
           raise TypeError("Task is not anti task")


    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            raise ValueError('Task does not exist')

    # For editing task
    # 1. Make sure taks exists (check if there is a task of that name)
    # 2. Ask what they want to change about the task
    # 3. Check if change creates conflicts (eg. not valid task type for that task class) or conflicts with other tasks (eg. overlap of datetime or name)

    # Check if a task exists by name. Returns task if it does, False otherwise
    def task_exists_by_name(self, taskName):
        for existing_task in self.tasks:
            if taskName == existing_task.name:
                return existing_task
        return False
    
    # Updates a tasks name. If the new name exists return False. True if change is successful
    def update_task_name(self, currentTaskName , newTaskName):
        newTask = self.task_exists_by_name(newTaskName)
        currentTask = self.task_exists_by_name(currentTaskName)
        # If task by the new name already exists return false, or there is currentTask does not exist
        if (newTask or not currentTask):
            return False
        
        # We can change the current task to 
        else:
            currentTask.name = newTaskName
            return True

    # Return a list of tasks for the next n days
    # Prompt user with How far in advance would you like to view your schedule
    def tasksForNextDays(self, days):
        res = []
        today = datetime.today()
        endDate = today + datetime.day(days)
        for task in self.tasks:
            if isinstance(task, RecurringTask):
                for occurence in task.occurences(datetime.today(), task.endDatetime):
                    if today <= occurence <= endDate:
                        occurenceName = 'Occurance of ' + task.name
                        singleOccurence = Task(occurenceName, task.type, )
                        res.append(singleOccurence)
            elif (today <= task.startDatetime.today() <= endDate):
                res.append(task)
        return task

            
        
    #   def importJson(self, jsonFile) (WIP):



    # def exportJson(self, skipKeys = True):
        #trying to open file and append the tasks to the file (WIP)
        '''
        try: 
            with open("schedule.json", "w") as outfile:
                for task in self.tasks:
                    json.dump(task__dict__, outfile)   
                json.dump(dictionary, outfile)
                '''


# YYYY MM DD
# Private methods
    def create_datetime(self, date, time):
        year = int(date / 10000)
        month = int(date / 100 % 100)
        day = int(date % 100)
        hours = int(time)
        minutes = (int(time - hours) * 60)
        
        return datetime(year, month, day, hours, minutes)
    
    def __tasks_completely_overlap(self, task1, task2):
        return (task1.startDatetime == task2.startDatetime and task2.duration == task2.duration)

    def __tasks_overlap(self, task1, task2):
        start1 = task1.startDatetime
        end1 = start1 + task1.duration

        start2 = task2.startDatetime
        end2 = start2 + task2.duration

        return max(start1, start2) < min(end1, end2)