# Exercise 1: Temperature Converter
def temperature_converter():
    print("""\nWelcome to Temperature Converter Program!
+------------------------+---------------+
| Conversion Type        |    Number     |
+------------------------+---------------+
| Celsius to Fahrenheit  |      1        |
| Fahrenheit to Celsius  |      2        |
+------------------------+---------------+""")
    # Ask the user to input a temperature.
    temperature = float(input("Enter Temperature: "))  
    # Ask the user to select the conversion type.
    conversion_type = int(input("Enter the corresponding number of the conversion type you want to select: "))   
    # Perform the appropriate conversion and print the result.
    if conversion_type == 1:
        # Celsius to Fahrenheit
        conversion = (9/5 * temperature) + 32
        print(f"Converted Temperature: {conversion:.2f}°F")
    elif conversion_type == 2:
        # Fahrenheit to Celsius
        conversion = 5/9 * (temperature - 32)
        print(f"Converted Temperature: {conversion:.2f}°C")
    else:
        print("Error. Invalid Input!")
  
# Exercise 2: Ohm’s Law Calculator
def ohms_calculator():
    print("""\nWelcome to Ohm'c Calculator Program!
+------------------------+---------------+
| Variable               |    Number     |
+------------------------+---------------+
| Voltage                |      1        |
| Current                |      2        |
| Resistance             |      3        |
+------------------------+---------------+""")
    # Ask the user wht they want to calculate
    choice = int(input("Enter the corresponding number of the variable you want to calculate: "))
    # Calculation for Voltage
    if choice == 1:
        current = float(input("Enter Current (in amperes): "))
        resistance = float(input("Enter Resistance (in ohms): "))
        answer = current * resistance
        print(f"Voltage = {answer:.2f}V")      
    # Calculation for Current
    elif choice == 2:
        voltage = float(input("Enter Voltage (in volts): "))
        resistance = float(input("Enter Resistance (in ohms): "))
        answer = voltage / resistance
        print(f"Current = {answer:.2f}A")     
    # Calculation for Resistance
    elif choice == 3:
        voltage = float(input("Enter Voltage (in volts): "))
        current = float(input("Enter Current (in amperes): "))
        answer = voltage / current
        print(f"Resistance = {answer:.2f}Ω")        
    else: 
        print("Error. Invalid Input!")
    
# Exercise 3:  Diamond Shape (advance topic):
def print_diamond(width):
    if width % 2 == 0:
        print("Error! Please provide an odd integer.")
    else:
        print("\nWelcome to Diamond Maker Program! This is your diamond.\n")
        # Make the diamond
        mid = width // 2
        for i in range(mid + 1):
            spaces = ' ' * (mid - i)
            stars = '*' * (2 * i + 1)
            print(spaces + stars)
        for i in range(mid - 1, -1, -1):
            spaces = ' ' * (mid - i)
            stars = '*' * (2 * i + 1)
            print(spaces + stars)

# This is the main function of the program, where I included all the error catchers to avoid repetitiveness   
def main():
    print("""Data Structure and Algorithm
Lab Activity: Python review
Programmed by: Mark Justine L. Apitan

+------------------------+---------------+
| Program                |    Number     |
+------------------------+---------------+
| Temperature Converter  |      1        |
| Ohm's Law Calculator   |      2        |
| Diamond Shape          |      3        |
+------------------------+---------------+""")
    try:
        # Ask the user Choice
        program_chosen = int(input("Enter the corresponding number of the program you want to select: "))
        if program_chosen == 1:
            temperature_converter()
        elif program_chosen == 2:
            ohms_calculator()
        elif program_chosen == 3:
            width = int(input("Enter the width you want (odd numbers only): "))
            print_diamond(width)
        else:
            print("Invalid Input!")
    # To catch all the errors
    except ValueError:
        print("Error. Invalid Input! Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error. Zero division detected! Current or Resistance cannot be zero.")
main()