# Count all letters, digits,
# and special symbols from a given
# string

# Given:

# str1 = "P@#yn26at^&i5ve"
# Expected Outcome:

# Total counts of chars, digits, and symbols

# Chars = 8
# Digits = 3
# Symbol = 4

str1 = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbol = 0

for char in str1:
    if char.isnumeric():
        digits += 1
    elif char.isalpha():
        chars += 1
    else:
        symbol += 1

print(chars, digits, symbol)
