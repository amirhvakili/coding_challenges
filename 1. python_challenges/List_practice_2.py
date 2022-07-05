# print the duplicates in the list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for index, value in enumerate(some_list):
    for i, v in enumerate(some_list):
        if (index == i):
            continue
        elif v == value and v not in duplicates:
            duplicates.append(value)

print(duplicates)
