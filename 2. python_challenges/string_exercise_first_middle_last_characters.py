# Create a string made of the first,
# middle and last character

# Write a program to create a
# new string made of an input string’s first,
# middle, and last character.

# Given:

# str1 = "James"
# Expected Output:

# Jms

str1 = "James"

if len(str1) % 2 == 0:
    print(
        f'The first character is {str1[0]} and the last character is {str1[len(str1)-1]} and there is no middle character')
else:
    print(
        f'The first character is {str1[0]}, the middle character is {str1[int(((len(str1)-1)/2))]} and the last character is {str1[len(str1)-1]}')
