# Define a function called LetterCapitalization that takes one parameter (a string)
def LetterCapitalization(strParam):
    # Split the input string into a list of words based on spaces
    strParam = strParam.split(' ')
    # Capitalize the first letter of each word and join them back into a single string
    opt = ' '.join([word.capitalize() for word in strParam])
    # Return the modified string with capitalized words
    return opt

# Testing the function with an input string
input_string = "hello world from group 4"
# Call the function and store the output
output = LetterCapitalization(input_string)
print(output)  # Output: "Hello World From Group 4"