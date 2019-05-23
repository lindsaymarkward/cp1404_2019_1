"""
Write a program to determine which is the largest file
in the current directory,
as defined by total number of characters in the file.
You will need to use the os module.
"""

import os

max_length = 0
filename_of_longest = ''

for filename in os.listdir('.'):
    try:
        file_object = open(filename)
    except IsADirectoryError:
        continue
    text = file_object.read()
    file_object.close()
    if len(text) > max_length:
        max_length = len(text)
        filename_of_longest = filename

print("{} is the longest file".format(filename_of_longest))
