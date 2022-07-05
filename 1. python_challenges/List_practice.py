some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Get all the duplicates of the above list using comprehension

duplicates = list({char for char in some_list if some_list.count(char) > 1})

print(duplicates)
