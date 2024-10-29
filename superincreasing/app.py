
#In this code, a super-increasing sequence (or superincreasing sequence) is a sequence of numbers where each element in the sequence is greater than the sum of all previous elements.

# Define a function called SuperIncreasing that takes one parameter (a list of numbers)
def SuperIncreasing(arr):
    # Loop through the list starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is less than or equal to the sum of all previous elements
        if arr[i] <= sum(arr[0:i]):
            # If the condition is met, return False as the list is not super-increasing
            return False
    # If no element violates the condition, return True as the list is super-increasing
    return True

# Testing the function with different inputs
# Call the function with [1, 3, 6, 13, 27] and print the result
#print(SuperIncreasing([1, 3, 6, 13, 54])) output=True
#print(SuperIncreasing([1, 2, 3, 4,]))     output=False 
#print(SuperIncreasing([1, 2, 5, 10,]))     output=True
