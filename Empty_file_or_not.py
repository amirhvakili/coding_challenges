import os

if os.stat('test.txt').st_size == 0:
    print('File is empty')
else:
    print('File is not empty')
