
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


operation = input("Enter the operation (+, -, *, /): ")

match operation:
    case "+":
        
        print(f"The result of {num1 + num2} is: ")
    case "-":
        
        print(f"The result of {num1 - num2} is: ")
    case "*":
        
        print(f"The result of {num1 * num2} is: ")
    case "/":
        if num2 != 0:
            
            print(f"The result of {num1 / num2} is: ")
        else:
            print("Error: Cannot divide by zero.")
    case _:
        print("Invalid operation entered.")
