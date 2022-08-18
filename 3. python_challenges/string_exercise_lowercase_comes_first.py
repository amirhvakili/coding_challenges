# Arrange string characters such that
# lowercase letters should come first

# Given string contains a combination
# of the lower and upper case letters.
# Write a program to arrange the characters
# of a string so that all lowercase letters
# should come first.

# Given:

# str1 = PyNaTive

# Expected Output: yaivePNT

str1 = 'PyNaTive'
str2 = 'plpdsWDdsaEE'


def lowers_first(string):
    for char in string:
        if char == char.lower():
            print(char, end='')

    for char in string:
        if char == char.upper():
            print(char, end='')
    print()


lowers_first(str1)
lowers_first(str2)
