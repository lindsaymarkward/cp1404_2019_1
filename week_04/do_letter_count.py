"""
Ask the user for their name
Tell them how many vowels are in their name
Example output

Name: Bobby McAardvark
Out of 16 letters, Bobby McAardvark has 4 vowels

Use the str.format() method for the last print.
"""

name = input("Name: ")
number_of_vowels = 0
for character in name.lower():
    if character in 'aeiou':
        number_of_vowels += 1

print("Out of {} letters, {} has {} vowels".format(len(name), name, number_of_vowels))
