# Find the sum of the series upto n terms

# Write a program to calculate the sum of
# series up to n term. For example, if n =5 the
# series will become
# 2 + 22 + 222 + 2222 + 22222 = 24690

# Given:

# # number of terms
# n = 5
# Expected output:

# 24690

from logging import exception


while True:
    try:
        user_input_number = int(
            input('Please enter a positive natural number between 1 to 9 (1 and 9 are accepted as well): '))
        if 1 <= user_input_number <= 10:
            first_number = user_input_number
            second_number = first_number * 10 + first_number
            all_numbers = [first_number, second_number]
            n = 5
            sum = first_number + second_number
            for i in range(n-2):
                first_number = second_number
                second_number = first_number * 10 + user_input_number
                all_numbers.append(second_number)
                sum += second_number

            print(f'numbers are: {all_numbers}')
            print(f'The sum of these numbers is: {sum}')
            break
        else:
            raise Exception()
    except:
        continue
