import os

print(len([file for file in os.listdir(
    './first_30_challenges/') if file.endswith('.py')]))
