# Count the total number of digits
# in a number

# Write a program to count
# the total number of digits
# in a number using a while loop.

# For example, the number is 75869,
# so the output should be 5.

import math

while True:
    try:
        number = int(input('Please insert a natural number: '))
        number_of_digits = 0

        while number > 0:
            number = math.trunc(number / 10)
            number_of_digits += 1
        print(f'number_of_digits: {number_of_digits}')
        break
    except:
        print('This is not a natural number. Please try again')
        continue
