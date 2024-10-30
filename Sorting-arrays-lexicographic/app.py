# Define a function named 'sort_array' that takes an array as input and returns it sorted.
def sort_array(arr):
    # Use the built-in sorted() function to sort the array in ascending order.
    # The sorted() function returns a new sorted list, leaving the original array unchanged.
    return sorted(arr)

# Test case 1: input array with unsorted integers.
input_array1 = [5, 1, 3, 4, 2, 8, 7, 6, 10]
# Call the sort_array function with the input_array1 and print the sorted result.
print(f"Example 1 - Sorted array: {sort_array(input_array1)}")  # Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 10]

# Test case 2: input array with negative and positive integers.
input_array2 = [-3, 1, -5, 4, 2, 0, -1, 3]
# Call the sort_array function with the input_array2 and print the sorted result.
print(f"Example 2 - Sorted array: {sort_array(input_array2)}")  # Expected Output: [-5, -3, -1, 0, 1, 2, 3, 4]

# Test case 3: input array that is already sorted in ascending order.
input_array3 = [1, 2, 3, 4, 5]
# Call the sort_array function with the input_array3 and print the sorted result.
print(f"Example 3 - Sorted array: {sort_array(input_array3)}")  # Expected Output: [1, 2, 3, 4, 5]
