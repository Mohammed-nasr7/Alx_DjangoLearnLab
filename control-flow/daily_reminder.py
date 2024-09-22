task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


reminder = f"'{task}' is a {priority} priority task"


match priority:
    case "high":
        reminder += " that requires immediate attention today!"
    case "medium":
        reminder += ". It's important, but not urgent."
    case "low":
       reminder += ". Consider completing it when you have free time."
    case _:
        reminder += ". Note: Priority not recognized."


if time_bound == "yes":
    reminder = f" Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"

if time_bound == "no":
    reminder = f" note: '{task}' is a {priority} priority task. Consider completing it when you have free time."    

    


print(reminder)
