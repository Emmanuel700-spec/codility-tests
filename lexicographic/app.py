# Define a function called lexicographic_sort that takes one parameter (a list of strings)
def lexicographic_sort(s):
    # Sort the list in lexicographic order (case-insensitive) and return it
    return sorted(s, key=str.upper)

# Testing the function with different inputs
print(lexicographic_sort(['apple', 'banana', 'cherry']))  # Output: ['apple', 'banana', 'cherry']
print(lexicographic_sort(['dog', 'antelope', 'cat']))  # Output: ['antelope', 'cat', 'dog']
print(lexicographic_sort(['zebra', 'monkey', 'lion']))  # Output: ['lion', 'monkey', 'zebra']
