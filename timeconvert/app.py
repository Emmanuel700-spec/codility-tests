#The TimeConvert function takes an integer num, representing a number of minutes, and converts it into hours and minutes in the format hours:minutes

# Define a function called TimeConvert that takes one parameter (an integer representing minutes)
def TimeConvert(num):
    # Check if the number of minutes is less than 60
    if num < 60:
        # If so, return the time as "0:num" (0 hours and num minutes)
        return '0:' + str(num)
    else:
        # Calculate hours by using integer division
        hr = num // 60
        # Calculate remaining minutes using modulo operator
        min = num % 60
        # Return the time as "hr:min" in string format
        return str(hr) + ':' + str(min)

#print(TimeConvert(70))
print(TimeConvert(30))
