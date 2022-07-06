# Display Fibonacci series up to 10 terms

# The Fibonacci Sequence is a series of
# numbers. The next number is found by
# adding up the two numbers before it.
# The first two numbers are 0 and 1.

# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21.
# The next number in this series above is
# 13+21 = 34.

# Expected output:

# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

def fibonacci(index):
    a = 0
    b = 1
    print(a, end=' ')
    print(b, end=' ')

    for i in range(1, index):
        c = a + b
        print(c, end=' ')
        a = b
        b = c


fibonacci(9)
