"""
Write code for a function that takes two lists:
a list of names
a corresponding list of ages
(That is, elements at the same list index represent the same person.)
The function should return the name of the oldest person in the list.
(Return the first name if multiple people have the same oldest age.)
"""


def main():
    names = ["William", "Jane", "Sven"]
    ages = [106, 34, 106]

    for i in range(len(names)):
        print("{:8} is {:3} years old".format(names[i], ages[i]))

    print("Oldest is {}".format(find_oldest(names, ages)))


def find_oldest(names, ages):
    maximum_age = ages[0]
    maximum_index = 0
    for i in range(len(ages)):
        if ages[i] > maximum_age:
            maximum_age = ages[i]
            maximum_index = i

    return names[maximum_index]


main()
