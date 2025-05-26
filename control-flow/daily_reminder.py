
# Prompt user for task details
task = input("Enter your task:")
priority = input("Priority(high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority
match priority:
    case "high":
        reminder = f"Reminder: {task} is a {priority} priority task"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"Reminder: {task} is a {priority} priority task."
    case _:
        reminder = f"Task: {task} (priority not specified)"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."