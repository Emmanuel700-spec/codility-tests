# Function to count each character in a string
# Output: An object (dictionary) containing the count of each character in the string
# Example: For input "aba", the output should be { 'a': 2, 'b': 1 }
# Edge Case: For an empty string "", the output should be an empty object {}

def count_characters(s):
    # Initialize an empty dictionary to store character counts
    char_count = {}
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is already in the dictionary
        if char in char_count:
            # If it is, increment its count by 1
            char_count[char] += 1
        else:
            # If it isn't, add it to the dictionary with a count of 1
            char_count[char] = 1
    
    # Return the dictionary containing the count of each character
    return char_count

# To test the function, you can run the following code:
print(count_characters("aba"))  # Expected output: {'a': 2, 'b': 1}
print(count_characters(""))     # Expected output: {}
print(count_characters("mississippi"))  # Expected output: {'m': 1, 'i': 4, 's': 4, 'p': 2}
