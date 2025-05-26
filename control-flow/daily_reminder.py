task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
timebound = input("Is it time-bound?(yes/no):")

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