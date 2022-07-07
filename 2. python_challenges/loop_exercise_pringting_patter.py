# Print the following pattern

# Write a program to print the
# following start pattern using the for loop

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

rows = 5

for i in range(1, rows + 1):
    print('* ' * i)

for i in reversed(list(range(1, rows))):
    print('* ' * i)
