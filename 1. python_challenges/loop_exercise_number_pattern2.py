# Write a program to use for loop
# to print the following reverse
# number pattern

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

while True:
    try:
        row = int(input('please insert the number of rows you want to have: '))
        print('Here is your beautiful pattern with the given rows:')
        column = row

        for i in range(1, row + 1):
            for j in range(column, 0, -1):
                print(j, end=' ')
            print('')
            column -= 1
        break
    except:
        print('This is not a valid number. Please try again.')
        continue
