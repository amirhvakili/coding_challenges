# Create a new string made of the first,
# middle, and last characters of each input
# string

# Given two strings, s1 and s2,
# write a program to return a new string
# made of s1 and s2’s first, middle,
# and last characters.

# Given:

# s1 = "America"
# s2 = "Japan"

# Expected Output:

# AJrpan

def new_string(s1, s2):
    if not int(len(s1)) % 2 == 0 and not int(len(s2)) % 2 == 0:
        new_str = s1[0] + s2[0]+s1[int((len(s1)-1) / 2)] + s2[int(
            (len(s2)-1) / 2)] + s1[int(len(s1))-1] + s2[int(len(s2))-1]
        return new_str
    else:
        return f'{s1} and {s2} can not be added together because the number of characters of one of your inputs is even'


s1 = "America"
s2 = "Japan"

print(new_string(s1, s2))
