import os

if (len([file for file in os.listdir(
        './1. python_challenges/') if file.endswith('.py')])) >= 30:
    print('Too many python files in a folder. Please create a new folder')
else:
    print('You can create more python files. No problem.')
