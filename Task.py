
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
from datetime import datetime, timedelta

# Parent Class Task Constructor
class Task():

    def __init__(self, name, type, startTime, duration, date):
        self.name = name
        self.type = type
        self.startDatetime = self.__create_datetime(date, startTime)
        self.duration = self.__create_datetime(duration)
        self.endDatetime = self.startDatetime + self.duration
    
    def __create_datetime(self, date, time):
        year = int(date / 10000)
        month = int(date / 100 % 100)
        day = int(date % 100)
        hours = int(time)
        minutes = (int(time - hours) * 60)
        
        return datetime(year, month, day, hours, minutes)
    
    def __create_timedelta(self, duration):
        # eg. duration = 3.25           hours = duration // 1          minutes = (duration % hours) * 60
        hours = int(duration)
        minutes = (int(duration-hours) * 60)
        return timedelta(hours=hours, minutes=minutes)
'''
Parameters:
    Same as Task (taskType = ['Visit', 'Shopping', 'Appointment'])
'''
class TransientTask(Task):
    def __init__(self, name, type, startTime, duration, date):
        super().__init__(name, type, startTime, duration, date)


'''
Parameters:
    Same as Task (taskType = ['Class', 'Study', 'Sleep', 'Exercise', 'Work', 'Meal'])
    +
    int endDate (YYYYMMDD)
    int frequency (eg. 1, 7)
'''
class RecurringTask(Task):
    def __init__(self, name, type, startTime, duration, date, endDate, frequency):
        super().__init__(name, type, startTime, duration, date)
        self.endDate = endDate
        # self.endDatetime = self.__create_datetime(endDate, duration)

        # Frequency represented by a timedelta object
        self.frequency = timedelta(days=frequency)

        # Method that generates occurences that fall within start and end dates
        def occurences(self, startDate, endDate):
            current_datetime = self.startDatetime
            while current_datetime.date() <= self.endDate:
                if startDate <= current_datetime.date() <= endDate:
                    yield current_datetime
                current_datetime += self.frequency


'''
Parameters:
    Same as Task (taskType = ['Cancellation'])
'''
class AntiTask(Task):
    def __init__(self, name, type, startTime, duration, date):
        super().__init__(name, type, startTime, duration, date)
        