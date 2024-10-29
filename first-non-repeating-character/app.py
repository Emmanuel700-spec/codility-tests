def first_non_repeating_letter(string):
    # Convert to lowercase for case-insensitive comparison
    lowercase_string = string.lower()
    # Count occurrences
    freq = {}

    # Populate the frequency dictionary
    for char in lowercase_string:
        freq[char] = freq.get(char, 0) + 1

    # Find the first character that appears only once
    for index, char in enumerate(lowercase_string):
        if freq[char] == 1:
            # Return the character in its original case
            return string[index]

    # If no non-repeating character is found, return an empty string
    return ""

# Test cases
print(first_non_repeating_letter("stress"))  # Output: "t"
print(first_non_repeating_letter("sTreSS"))  # Output: "T"
print(first_non_repeating_letter("aabbcc"))   # Output: ""
