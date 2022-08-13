# Find the largest item from a given list

# x = [4, 6, 8, 24, 12, 2]

# Expected Output: 24

x = [4, 6, 8, 24, 12, 2]


def maximum(li):
    max = 0
    for number in li:
        if number > max:
            max = number
    return max


print(maximum(x))
