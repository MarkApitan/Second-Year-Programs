# Lab exercise 1

# from a given list of integers, create a new list using comprehension that will compute the square of odd integer elements.

# sample calls
# [2,4,3] == [9]
# [0,0,1,1] == [1,1]

def square_of_odds(lst):
    # List comprehension to square only the odd numbers in the input list
    return [item ** 2 for item in lst if item % 2 != 0]

# Sample lists
list_1 = [2, 4, 3]
list_2 = [0, 0, 1, 1]

# Print the result of squaring the odd numbers in the sample lists
print(square_of_odds(list_1))
print(square_of_odds(list_2)) 