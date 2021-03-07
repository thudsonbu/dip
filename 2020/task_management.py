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
        print("Current Arr " + str(task))
        try:
            cooldowns = task_cooldowns[task]
            if cooldowns == 0:
                task_cooldowns[task] = cooldown + 1
            else:
                extracooldowns += cooldowns
                for i in range(cooldowns):
                    for dec_task in task_cooldowns:
                        task_cooldowns[dec_task] -= 1
                        print("Task " + str(dec_task) +
                              " Extra cooldowns " + str(task_cooldowns[dec_task]))
                task_cooldowns[task] = cooldowns + 1
        except:
            task_cooldowns[task] = cooldown + 1
            print("New Task " + str(task))
        for decrement_task in task_cooldowns:
            if task_cooldowns[decrement_task] > 0:
                task_cooldowns[decrement_task] -= 1
                print("Task " + str(decrement_task) + " Cooldowns " +
                      str(task_cooldowns[decrement_task]))
    return len(arr) + extracooldowns


def findTime(tasks, cooldown):
    lastPos = {}
    current = 0

    for task in tasks:
        if task in lastPos:
            if current - lastPos[task] <= cooldown:
                current = cooldown + lastPos[task] + 1
        lastPos[task] = current
        current = current + 1

    return current
        

print(findTime([1, 1, 2, 1], 2))