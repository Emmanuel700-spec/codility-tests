# Define a function called ReverseString that takes one parameter (a string)
def ReverseString(str):
    # Use slicing to reverse the string and return it
    return str[::-1]

# Testing the function with different inputs
# Call the function with "coderbyte" and print the result
print(ReverseString("coderbyte"))  # Output: etybredoc

# Call the function with "I Love Code" and print the result
print(ReverseString("I Love Code"))  # Output: edoC evoL I
print(ReverseString("happy 21st birthday"))