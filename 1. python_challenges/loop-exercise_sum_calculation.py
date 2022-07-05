# Write a program to accept a number
# from a user and calculate the sum
# of all numbers from 1 to a given number

# For example, if the user entered 10
# the output should be 55
# (1+2+3+4+5+6+7+8+9+10)

# Expected Output:

# Enter number 10
# Sum is:  55

user_number_input = int(input('Please insert a number: '))

sum_number = 0

for number in range(user_number_input + 1):
    sum_number += number

print(f'The sum of numbers from 1 to {user_number_input} is {sum_number}')
