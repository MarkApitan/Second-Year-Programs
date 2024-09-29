"""Lab 2 Exercise 1
A teacher named Mrs. Rivera who loved making math fun for her students. One day, a student named Mia asked how to calculate powers, like (2^7). Mrs. Rivera explained, “Imagine you need to multiply 2 by itself seven times. We can solve this using a python code utilizing  special method called recursion to solve this,” 
Can you help the class of Mrs. Rivera by providing the recursive method to calculate powers?
"""
def calculate_powers(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * calculate_powers(base, exponent - 1)

invalid = True
while invalid:
    try:
        base = float(input("Enter a number to raise to a power: "))
        exponent = int(input("Enter the exponent: "))
        invalid =False
    except ValueError:
        print("Invalid Input. Please Enter a Number")

print(calculate_powers(base,exponent))