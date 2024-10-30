# Import the Counter class from the collections module.
# Counter helps count the occurrences of each character in the string.
from collections import Counter

# Define a function that finds the first non-repeating character in a string.
def first_non_repeating_char(s: str) -> str:
    # Create a counter for all characters in the string, converted to lowercase.
    # This counts the frequency of each character, ignoring case sensitivity.
    lower_count = Counter(s.lower())
    
    # Iterate through each character in the original string.
    for char in s:
        # Check if the character (in lowercase) has a count of 1, indicating it's non-repeating.
        if lower_count[char.lower()] == 1:
            # If found, return the original character (preserving its case).
            return char
    
    # If no non-repeating character is found, return an empty string.
    return ""

# Test cases
# Example 1: Mixed-case input with a non-repeating character "T"
input_string1 = "sTreSS"
result1 = first_non_repeating_char(input_string1)
print(f"Example 1 - Input: '{input_string1}' -> First non-repeating character: '{result1}'")  # Expected Output: "T"

# Example 2: All characters repeat, so the output should be an empty string.
input_string2 = "aabbcc"
result2 = first_non_repeating_char(input_string2)
print(f"Example 2 - Input: '{input_string2}' -> First non-repeating character: '{result2}'")  # Expected Output: ""

# Example 3: First non-repeating character is "H"
input_string3 = "HeLloWorld"
result3 = first_non_repeating_char(input_string3)
print(f"Example 3 - Input: '{input_string3}' -> First non-repeating character: '{result3}'")  # Expected Output: "H"
