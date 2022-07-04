# Exercise 2:
# Write a program to print the
# following number pattern using a loop.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for row in range(1, 7):
    for i in range(1, row):
        print(i, end=' ')
    print('')
