
# Prompt user for task details
task = input("Enter your task:")
priority = input("Priority(high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high' | 'medium':
        if timebound == 'yes':
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a {priority} priority task.")
    case 'low':
        if timebound == 'yes':
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: {task} is an unspecified priority task.")