# Lab exercise 2

# Using comprehension,create a new list of tuples from two given lists:

# Sample calls
# list1[1,2,3]
# list2["mark","alice","john]

# result: listOfTuple[(1,"mark"),(2,"alice"),(3,"john")] 

# Define two lists
list_1 = [1, 2, 3]
list_2 = ["mark", "alice", "john"]

# Create a list of tuples by pairing elements from both lists using list comprehension
list_of_tuple = [(list_1[i], list_2[i]) for i in range(len(list_1))]

# Print the resulting list of tuples
print(list_of_tuple)