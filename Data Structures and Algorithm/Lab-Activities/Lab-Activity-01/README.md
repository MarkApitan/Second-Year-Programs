# Lab Activity: Python review 
Deadline: September 22, 2024 11:59pm
[Click here to see the code of the program](https://github.com/MarkApitan/Second-Year-Programs/blob/main/Data%20Structures%20and%20Algorithm/Lab-Activities/Lab-Activity-01/lab-activity-one.py)

# Exercise 1: Temperature Converter
Create a program that converts temperatures between Celsius and Fahrenheit.
Instructions:
1.	Ask the user to input a temperature.
2.	Ask the user to select the conversion type: from Celsius to Fahrenheit or from Fahrenheit to Celsius.
3.	Perform the appropriate conversion and print the result.
## Sample Run of the program
![image](https://github.com/user-attachments/assets/f88b91ea-403a-49ff-9a9c-9e609193f6a7)
![image](https://github.com/user-attachments/assets/285d273c-ca0f-4e01-8272-c94b36ea3515)

# Exercise 2: Ohm’s Law Calculator
Instructions:
1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
2.	Based on their choice, prompt the user to input the appropriate values.
3.	Use Ohm's Law to calculate the missing variable and display the result.
4.	Handle cases where division by zero might occur.
## Sample Run of the program
![image](https://github.com/user-attachments/assets/5d43d70e-5375-4fdd-864a-28ff29d2fd5d)
## Error Catch for zero division 
![image](https://github.com/user-attachments/assets/388ed776-abb3-494b-ac0c-5f67c14d6b38)

# Exercise 3:  Diamond Shape (advance topic):

Write a Python function named print_diamond that takes an odd integer n as an argument and prints a diamond shape with a width of n using the * character.
For n = 5, the output should be:
```
  *
 ***
*****
 ***
  *
```
Note: if an even number is passed, the function should return "Please provide an odd integer." 
## Sample Run of the program
![image](https://github.com/user-attachments/assets/c48b2145-5887-40e3-8233-711923152654)
## Error catch if the user input even number
![image](https://github.com/user-attachments/assets/6b33f600-79ec-4d52-9dc5-1041283c3f5b)

# Take Aways
I tried to make this program as clean as possible, and I feel successful in doing so. My proudest achievement is when I found a way to catch all possible errors in the program by ensuring all inputs are integers or floats. This way, I only needed to check for ValueError and place the error handling in the main function to save lines and space in the program.
