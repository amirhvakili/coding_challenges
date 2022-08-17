import os

files = [file for file in os.listdir(
    './3. python_challenges/') if file.endswith('.py')]
if len(files) >= 25:
    print(len(files))
    print('Too many python files in a folder. Please create a new folder')
else:
    print(len(files))
    print('You can create more python files. No problems.')
