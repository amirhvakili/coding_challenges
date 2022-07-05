# Display numbers from a list using loop
# Write a program to display only
# those numbers from a list that
# satisfy the following conditions

# 1- The number must be divisible by five
# 2- If the number is greater than 150,
# then skip it and move to the
# next number
# 3- If the number is greater than 500,
# then stop the loop


# Given:
# numbers = [12, 75, 150, 180, 145, 525, 50]


# Expected output:
# 75
# 150
# 145

numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number > 500:
        break
    elif number > 150:
        continue
    elif number % 5 == 0:
        print(number)
