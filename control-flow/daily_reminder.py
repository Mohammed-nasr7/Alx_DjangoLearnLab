
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case "high":
        reminder = f"Finish project report' is a high priority task that requires immediate attention today! {task}"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"Low priority task: {task}'."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low"


if time_bound == "yes":
    reminder += " Read a book' is a low priority task. Consider completing it when you have free time."


print(reminder)
