# Mark Justine L. Apitan
# Lab Activity: Python review

# Exercise 1: Temperature Converter
def temperature_converter():
    print("""
Select Conversion Type
+------------------------+---------------+
| Type                   | Enter Number  |
+------------------------+---------------+
| Celsius to Fahrenheit  |      1        |
| Fahrenheit to Celsius  |      2        |
+------------------------+---------------+""")
    try:
        # Ask the user to select the conversion type.
        conversion_type = int(input("Enter the corresponding number of the conversion type you want to select: "))
        # Ask the user to input a temperature (can be float for decimal values).
        temperature = float(input("Enter Temperature: "))
        
        # Perform the appropriate conversion and print the result.
        if conversion_type == 1:
            # Celsius to Fahrenheit
            conversion = (9/5 * temperature) + 32
            print(f"Converted: {conversion:.2f}°F")
        elif conversion_type == 2:
            # Fahrenheit to Celsius
            conversion = 5/9 * (temperature - 32)
            print(f"Converted: {conversion:.2f}°C")
        else:
            print("Error. Invalid Input!")
    except ValueError:
        print("Error. Invalid Input! Please enter a valid number.")

# Exercise 2: Ohm’s Law Calculator
def ohms_calculator():
    print("""
+------------------------+---------------+
| Variable               | Enter Number  |
+------------------------+---------------+
| Voltage                |      1        |
| Current                |      2        |
| Resistance             |      3        |
+------------------------+---------------+""")
    try:
        choice = int(input("Enter the corresponding number of the variable you want to calculate: "))
        
        # Calculation for Voltage (V = I * R)
        if choice == 1:
            current = float(input("Enter Current (in amperes): "))
            resistance = float(input("Enter Resistance (in ohms): "))
            answer = current * resistance
            print(f"Voltage = {answer:.2f}V") 
        
        # Calculation for Current (I = V / R)
        elif choice == 2:
            voltage = float(input("Enter Voltage (in volts): "))
            resistance = float(input("Enter Resistance (in ohms): "))
            answer = voltage / resistance
            print(f"Current = {answer:.2f}A")
        
        # Calculation for Resistance (R = V / I)
        elif choice == 3:
            voltage = float(input("Enter Voltage (in volts): "))
            current = float(input("Enter Current (in amperes): "))
            answer = voltage / current
            print(f"Resistance = {answer:.2f}Ω")
        
        else: 
            print("Error. Invalid Input!")
    
    except ValueError:
        print("Error. Invalid Input! Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error. Zero division detected! Current or Resistance cannot be zero.")
