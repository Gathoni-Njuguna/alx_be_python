task = input("Enter a task description: ")
priority = input("What is the task priority (high/medium/low): ").lower()
timebound = input("Is the task time bound (yes/no): ").lower()

match priority:
    case 'high':
        if timebound == 'yes':
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a {priority} priority task.")
    case 'medium':
        if timebound == 'yes':
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a {priority} priority task.")
    case 'low':
        if timebound == 'yes':
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print(f"Note: {task} is an unspecified priority task.")