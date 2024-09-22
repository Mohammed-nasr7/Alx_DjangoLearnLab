
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")





match priority:
    case "high":
        reminder = f" {task} that requires immediate attention today!"
    case "medium":
        reminder = f"{task} It's important, but not urgent."
    case "low":
       reminder = f"{task} Consider completing it when you have free time."
    case _:
        reminder = f"{task} Note: Priority not recognized."


if time_bound == "yes":
    reminder += f" Reminder:  priority task that requires immediate attention today!"

if time_bound == "no":
    reminder += f" note:  priority task. Consider completing it when you have free time."    

    


print(reminder)