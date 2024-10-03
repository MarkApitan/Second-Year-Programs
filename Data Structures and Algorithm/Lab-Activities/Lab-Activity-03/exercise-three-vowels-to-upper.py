# Lab exercise 3
# Provide a list comprehension that implementation for a function called vowelsToUpper with the following signature:

# method name : vowelsToUpper
# input argument : String 
# return argument : String

# vowelsToUpper must return a version of its String argument with all its vowels changed to their uppercase forms. Nonvowel characters stay as is.

# Sample Calls
# vowelsToUpper "" == ""
# vowelsToUpper "Hello, world!" == "HEllO, wOrld!"
# vowelsToUpper "hello hi bye" == "hEllO hI byE"

def vowels_to_upper(string):
    # Convert vowels to uppercase using list comprehension
    new_string = ''.join([char.upper() if char in ["a","e","i","o","u"] else char for char in string])
    return new_string

# Test cases 
print(vowels_to_upper(""))  
print(vowels_to_upper("Hello, world!")) 
print(vowels_to_upper("hello hi bye"))  