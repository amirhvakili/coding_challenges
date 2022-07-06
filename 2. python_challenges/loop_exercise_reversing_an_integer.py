# Reverse a given integer number
# Given:

# 76542

# Expected output:

# 24567

number = 76542
number_reversed = ''

for num in reversed(str(number)):
    number_reversed += num
print(int(number_reversed))
