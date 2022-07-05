# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Persian', 8)
cat2 = Cat('Russian', 6)
cat3 = Cat('Asian', 15)
ages = [cat1.age, cat2.age, cat3.age]

# 2 Create a function that finds the oldest cat


def find_max_age(*ages):
    return max(ages)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(
    f"The oldest cat is {find_max_age(cat1.age, cat2.age, cat3.age)} years old.")
