# Create a recursive function
# Write a program to create a
# recursive function to
# calculate the sum of numbers from 0 to 10.

# A recursive function is
# a function that calls itself again and again.

# Expected Output:

# 55


def recrusive_function(a, b, addition):
    init = addition
    a = a + 1
    addition = init + a

    while a < b:
        return recrusive_function(a, b, addition)
    else:
        return addition


result = recrusive_function(0, 10, 0)
print(result)
