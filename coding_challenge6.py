# creating a function that gets a list and
# returns the highest even number in that list


def highest_even(li):
    max = 0
    for item in li:
        if(item % 2 == 0 and item > max):
            max = item

    return max


print(highest_even([10, 4, 5, 6, 9, 3]))
