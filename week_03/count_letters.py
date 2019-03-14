from string import ascii_lowercase


def count_letters(string):
    """Count the letters in string"""
    count = 0
    for character in string.lower():
        if character in ascii_lowercase:
            count += 1
    # print(count)
    return count


# print(count_letters("abc1_ 2 3-DEF"))
# print(count_letters("0123"))
# name = input("Name: ")
# print(count_letters(name))

assert count_letters("0123") == 0
assert count_letters("hello") == 5

print(count_letters("hello"))