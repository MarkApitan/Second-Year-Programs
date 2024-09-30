def create_square(length):
    for i in range (length):
        if i == 0 or i == length -1:
            print (("*") * length)
        else:
            print(("*") + (" ")* (length - 2) + ("*"))

is_on =  True
while is_on:
    try:
        length = int(input("Enter the side length of the square: "))
        create_square(length)
        is_on = False
    except ValueError:
        print("Invalid Input. Please enter a valid number.")