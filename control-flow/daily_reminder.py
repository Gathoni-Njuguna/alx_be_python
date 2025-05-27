
# Prompt user for task details
task = input("Enter your task:")
priority = input("Priority(high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"{task} is a {priority} priority task"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"{task} is a {priority} priority task"
    case _:
        reminder = f"Task: {task} (priority not specified)"

# Modify reminder if time-bound
if time_bound == "yes":
   print("Reminder:", reminder, " that requires immediate attention today!")
else:
   print("Note:", reminder,"consider completing it when you have free time.")

