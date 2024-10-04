FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  
CELSIUS_TO_FAHRENHEIT_OFFSET = 32  

def convert_to_celsius(fahrenheit):
    """
    تقوم هذه الدالة بتحويل درجة الحرارة من فهرنهايت إلى درجة مئوية.
    Parameters:
        fahrenheit (float): درجة الحرارة بالفهرنهايت.
    Returns:
        float: درجة الحرارة بعد التحويل إلى درجة مئوية.
    """
   
    celsius = (fahrenheit - CELSIUS_TO_FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    تقوم هذه الدالة بتحويل درجة الحرارة من درجة مئوية إلى فهرنهايت.
    Parameters:
        celsius (float): درجة الحرارة بالدرجة المئوية.
    Returns:
        float: درجة الحرارة بعد التحويل إلى فهرنهايت.
    """
   
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_OFFSET
    return fahrenheit

def main():
    """
    الدالة الرئيسية للتفاعل مع المستخدم، والتي تتعامل مع إدخال درجة الحرارة
    واختيار نوع التحويل المطلوب.
    """
    try:
    
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

   
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
       
        converted_temp = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_OFFSET
        print(f"{temperature}°C is {converted_temp}°F")

    elif unit == 'F':
       
        converted_temp = (temperature - CELSIUS_TO_FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{temperature}°F is {converted_temp}°C")

    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
