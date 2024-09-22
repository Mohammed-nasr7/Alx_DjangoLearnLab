task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")





match priority:
    case "high":
        reminder = f" {task} is a high priority task"
    case "medium":
        reminder = f"{task} ia s medium priority task"
    case "low":
       reminder = f"{task} is a low priority task"
    case _:
        reminder = "invalid priority entered"


if time_bound == "yes" and priority in ["high", "medium" , "low"] :
    reminder += "that requirments immediate attention today!"

elif time_bound == "no" and priority in ["high", "medium" , "low"]:
    reminder += f"consider completing it when you have free time"  
else:
    print("reminder:" , reminder )
