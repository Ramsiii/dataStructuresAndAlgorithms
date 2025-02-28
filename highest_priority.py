# function to remove and return the task with the highest priority from a dictionary

def get_highest_priority_task(tasks):
    max_priority = max(tasks.values())
    sorted_tasks = dict(sorted(tasks.items()))
    for task in sorted_tasks:
        if sorted_tasks[task] == max_priority: 
            priority_task = task
            # remove task from original dict
            tasks.pop(priority_task)
            # return the priority task
            return priority_task

if __name__ == "__main__":
    
    tasks = {"Dishes": 8, "Cook": 10, "Eat": 9, "Clean Surfaces": 10, "Sweep": 7}
    print(tasks)
    perform_task = (get_highest_priority_task(tasks))
    print(perform_task)

    perform_task = (get_highest_priority_task(tasks))
    print(perform_task)

    perform_task = (get_highest_priority_task(tasks))
    print(perform_task)

    print(tasks)