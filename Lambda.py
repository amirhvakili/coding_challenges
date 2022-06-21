my_list = [5, 4, 3]

# each element of the list is squared by 2
print(list(map(lambda item: item ** 2, my_list)))

# List Sorting using lambda function
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key=lambda item: item[1]))
