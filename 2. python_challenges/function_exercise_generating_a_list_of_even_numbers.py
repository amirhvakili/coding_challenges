# Generate a Python list of all
# the even numbers between 4 to 30
# Expected Output:

# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# Solution 1:

# def generate_list():
#     i = 4
#     my_list = []
#     while i < 30:
#         if i % 2 == 0:
#             my_list.append(i)
#         i += 1
#     return my_list


# print(generate_list())

# Solution 2

print(list(range(4, 30, 2)))
