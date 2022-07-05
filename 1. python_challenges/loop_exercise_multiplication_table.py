# Exercise 4: Write a program to print
# multiplication table of a given number
# For example, num = 2 so the output
# should be

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

users_input = int(input('Please enter a number: '))

print(f'The multiplication table for {users_input} is:')

for number in range(1, 11):
    print(number * users_input)
