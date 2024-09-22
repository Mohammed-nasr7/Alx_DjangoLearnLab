task = input("enter your task ")
priority = input( "priority (high/medium/low)")
time_bound = input("Is it time-bound?")

match  priority :
    case "high" :
        reminder = f"High priority task: {task}"
    case "medium"  :
          reminder = f"Medium priority task: {task}"
    case "low" :
          reminder = f"Low priority task: {task}"
    case _:
        reminder = "Invalid priority enter high, medium, or low."  

if time_bound == "yes":
    reminder += " This requires immediate attention today!"

print(reminder)
             
   

