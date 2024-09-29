is_on = True
while is_on:
    try:
        size = int(input("Enter the size of the array: "))
        elements = input("Enter the elements of the array: ").split()
        
        if size != len(elements):
            print("Size doesn't match the number of elements.")
        else:
            for element in elements:
                print(int(element) ** 3)
            is_on = False  # Exit the loop when input is valid
    except ValueError:
        print("Invalid Input. Please enter a valid number.")