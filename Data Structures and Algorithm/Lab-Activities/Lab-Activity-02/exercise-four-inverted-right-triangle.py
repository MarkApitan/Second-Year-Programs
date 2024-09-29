def draw_inverted_triangle(height):
    for i in range(height, 0, -1):
        print("*" * i)

is_on = True
while is_on:
    try:
        height = int(input("Enter the height of the triangle: "))
        if height > 0:
            draw_inverted_triangle(height)
            is_on = False
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")