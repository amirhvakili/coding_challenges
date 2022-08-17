# Append new string in the middle of
# a given string

# Given two strings, s1 and s2.
# Write a program to create a new
# string s3 by appending s2 in the
# middle of s1.


# Given:

# s1 = "Ault"
# s2 = "Kelly"
# Expected Output:

# AuKellylt

def append_middle(s1, s2):

    if int(len(s1)) % 2 == 0:
        new_string = s1[:int(len(s1)/2)] + s2 + s1[int(len(s1)/2):]
        print(new_string)
    else:
        print(
            f'Can not add {s2} in the middle of {s1} because the length of {s1} is not even')


s1 = "Ault"
s2 = "Kelly"

append_middle(s1, s2)
