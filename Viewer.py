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
        
