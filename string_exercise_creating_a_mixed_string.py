# Create a mixed String using the
# following rules


# Given two strings, s1 and s2.
# Write a program to create a new string s3
# made of the first char of s1, then the
# last char of s2, Next, the second char
# of s1 and second last char of s2, and
# so on. Any leftover chars go at the end
# of the result.

# Given:

# s1 = "Abc"
# s2 = "Xyz"

# Expected Output: AzbycX

# My_solution:

# s1 = "Abc"
# s2 = "Xyz"

# s1_chars_list = list(s1)
# s2_chars_list = list(s2)
# s2_chars_list.reverse()

# joined_characters = []
# i = 0
# if len(s2_chars_list) >= len(s1_chars_list):
#     for char in s1_chars_list:
#         joined_characters.append(char + s2_chars_list[i])
#         i += 1
# else:
#     for char in s2_chars_list:
#         joined_characters.append(s1_chars_list[i] + char)
#         i += 1

# new_list = ''.join(joined_characters)

# if len(s2_chars_list) > len(s1_chars_list):
#     leftover = ''.join(s2_chars_list[len(s1_chars_list):len(s2_chars_list)])
#     print(new_list + leftover)
# elif len(s1_chars_list) > len(s2_chars_list):
#     leftover = ''.join(s1_chars_list[len(s2_chars_list):len(s1_chars_list)])
#     print(new_list + leftover)
# else:
#     print(new_list)


# Solution 2:
s1 = "Abc"
s2 = "Xyz"

s2 = s2[::-1]
result = ''

length = len(s1) if len(s1) > len(s2) else len(s2)

for i in range(length):
    if i < len(s1):
        result += s1[i]
    if i < len(s2):
        result += s2[i]
print(result)
