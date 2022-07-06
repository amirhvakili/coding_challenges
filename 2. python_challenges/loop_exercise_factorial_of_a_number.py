# Find the factorial of a given number
# Write a program to use the loop to find
# the factorial of a given number.

# The factorial (symbol: !) means to
# multiply all whole numbers from the
# chosen number down to 1.

# For example: calculate the factorial of 5

# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:

# 120

while True:
    try:
        number = int(input('Please enter a positive natural number here: '))
        if number == 0 or number == 1:
            print(f'The factorial of the given number is: 1')
        elif number > 1:
            for num in range(1, number):
                number = num * number
            print(f'The factorial of the given number is: {number}')
        elif number < 0:
            print('The factorial for negative numbers does not exist')
            continue
        break
    except:
        print('Enter a positive natural number. Please try again.')
        continue
