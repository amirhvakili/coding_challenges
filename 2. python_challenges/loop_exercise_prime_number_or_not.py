# Write a program to display all prime
# numbers within a range
# Note: A Prime Number is a number
# that cannot be made by multiplying
# other whole numbers. A prime number is
# a natural number greater than 1 that is
# not a product of two smaller
# natural numbers

# Examples:

# 6 is not a prime mumber because it can
# be made by 2×3 = 6
# 37 is a prime number because
# no other whole numbers multiply
# together to make it.

# Given:

# # range
# start = 25
# end = 50

# Expected output:

# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47

while True:
    try:
        users_number1, users_number2 = input(
            'Please insert two natural numbers (seperate your numbers with a comma): ').split(',')

        # User's inputs are converted into integers here
        users_number1 = int(users_number1)
        users_number2 = int(users_number2)
        for number in range(users_number1, users_number2 + 1):
            try:
                if(number == 1):
                    continue
                else:
                    for num in range(2, number):
                        if(not number % num == 0 and not num == number - 1):
                            continue
                        elif(num == number - 1 and not number % num == 0):
                            print(number)
                        else:
                            raise Exception()
            except:
                continue
        break

    except:
        print('Please insert your numbers correctly')
        continue
    finally:
        print('Done!')
