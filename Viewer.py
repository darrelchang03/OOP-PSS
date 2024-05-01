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

    # Private Methods
        