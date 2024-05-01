
'''
Parameters:
    String name MUST BE UNIQUE
    String type 
    float startTime (24 hr clock rounded to nearest 15 min. eg. 7:45 PM == 19.75)
    float duration (same format as startTime)
'''

import Model
import Task
import Viewer
import Controller

class Task():

# Parent Class Task Constructor

    def __init__(self, name, type, startTime, duration):
        self.name = name
        self.type = type
        self.startTime = startTime
        self.duration = duration
    

'''
Parameters:
    Same as Task (taskType = ['Visit', 'Shopping', 'Appointment'])
    +
    int date (YYYYMMDD)
'''
class TransientTask(Task):
    def __init__(self, name, type, startTime, duration, date):
        super().__init__(name, type, startTime, duration)
        self.date = date


'''
Parameters:
    Same as Task (taskType = ['Class', 'Study', 'Sleep', 'Exercise', 'Work', 'Meal'])
    +
    int endDate (YYYYMMDD)
    int frequency (eg. 1, 7)
'''
class RecurringTask(Task):
    def __init__(self, name, type, startTime, duration, startDate, endDate, frequency):
        super().__init__(name, type, startTime, duration)
        self.startDate = startDate
        self.endDate = endDate
        self.frequency = frequency

'''
Parameters:
    Same as Task (taskType = ['Cancellation'])
    +
    int date (YYYYMMMDD)
'''
class AntiTask(Task):
    def __init__(self, name, type, startTime, duration, date):
        taskType = 'Cancellation'
        super().__init__(name, type, startTime, duration, date)
        self.date = date