"""
Ask the user for a string and print out whether this string is a palindrome or
not. (A palindrome is a string that reads the same forwards and backwards.)
"""

def palindrome(str):
    # Reverse the string by creating a slice that starts at the end of the string, and moves backwards.
    reversedStr = str[::-1]
    if (str == reversedStr):
        return True

    return False

# Ask the user to input a word
word = input("Please input a string:")
print(palindrome(word))
