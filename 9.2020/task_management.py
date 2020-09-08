# Hi, here's your problem today. This problem was recently asked by AirBNB:

# We have a list of tasks to perform, with a cooldown period. We can do multiple of these at the same time, but we cannot run the same task simultaneously.

# Given a list of tasks, find how long it will take to complete the tasks in the order they are input.
# tasks = [1, 1, 2, 1]
# cooldown = 2
# output: 7 (order is 1 _ _ 1 2 _ 1)


def findTime(arr, cooldown):
    extracooldowns = 0
    task_cooldowns = {}
    for task in arr:
        for task, cooldowns in task_cooldowns.items():
            print("Task " + str(task) + " Cooldowns " + str(cooldowns))
            if task_cooldowns[task] > 0:
                task_cooldowns[task] -= 1
        try:
            cooldowns = task_cooldowns[task]
            if cooldowns == 0:
                task_cooldowns[task] = cooldown
            else:
                extracooldowns += cooldowns
                for i in range(cooldowns):
                    for task, cooldowns in task_cooldowns.items():
                        task_cooldowns[task] -= 1
        except:
            task_cooldowns[task] = cooldown
        print("/////////")
    return len(arr) + extracooldowns
        

print(findTime([1, 1, 2, 1], 2))