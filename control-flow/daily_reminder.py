
# Prompt user for task details
task = input("Enter your task: ")
priority = input("Enter priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Process task based on priority
match priority:
    case "high":
        reminder = f"High priority task: {task}"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"Low priority task: {task}"
    case _:
        reminder = f"Task: {task} (priority not specified)"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."