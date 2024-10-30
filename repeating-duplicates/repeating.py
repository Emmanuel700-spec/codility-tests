# Define a function named 'duplicates' that checks if a list contains duplicate elements.
def duplicates(nums):
    # Convert the list 'nums' to a set and compare its length with the original list.
    # Sets do not allow duplicates, so if any duplicates are in 'nums',
    # the length of 'set(nums)' will be shorter than the length of 'nums'.
    return len(nums) != len(set(nums))

# Test case 1: array1 contains duplicate elements (3 and 2 appear twice).
array1 = [1, 2, 3, 3, 4, 5, 2]
# The function should return True since there are duplicates in array1.
print(duplicates(array1))  # Output: True

# Test case 2: array2 has no duplicate elements.
array2 = [1, 2, 3, 4, 5]
# The function should return False as there are no duplicates in array2.
print(duplicates(array2))  # Output: False
