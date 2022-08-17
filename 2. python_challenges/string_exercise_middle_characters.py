# Create a string made of the middle three
# characters

# Write a program to create a new string
# made of the middle three characters
# of an input string.

# Given:

# Case 1

# str1 = "JhonDipPeta"
# Output = Dip


# Case 2

# str2 = "JaSonAy"
# Output = Son

str1 = 'JhonDipPeta'

str2 = "JaSonAy"


def middle_three_characters(string):
    if not int(len(string)) % 2 == 0:
        middle_character_index = int((len(string) - 1) / 2)
        new_string = string[middle_character_index -
                            1: middle_character_index + 2]
        return new_string
    else:
        return 'Number of characters is even. Therefore there is no middle three characters!'


print(middle_three_characters(str1))
print(middle_three_characters(str2))
print(middle_three_characters('even'))
