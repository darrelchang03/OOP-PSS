import Model
from Task import *

def main():
    model = Model.Model()
    task = Task("test", "lol", 12.00, 1.25, 20241028)
    model.add_task(task)
    recur = RecurringTask("recur", "lol", 13.25, 1.25, 20241028, 20241212, 7)
    model.add_task(recur)
    
    # task2 = Task("test2", "lol", 13.25, 1.25, 20241028)
    # model.add_task(task2)
    # anti = AntiTask()
if __name__ == "__main__":
    main()