from week_12.guitar import Guitar
import doctest


# g = Guitar("Guitar", 2010, 120.50)

def add(x, y):
    return x + y


assert add(2, 2) == 4
assert add(5, 6) == 11


# print(add(2, 2))
# print(add(5, 6))

def is_odd(x):
    return x % 2 == 1


assert is_odd(3)
assert not is_odd(4)


def is_adult(age):
    """
    Determine if age represents an adult
    >>> is_adult(18)
    True
    >>> is_adult(17)
    False
    >>> is_adult(42)
    True
    """
    return age >= 18


def ozify(phrase):
    """
    >>> ozify("How ya going")
    'How ya going, eh?'
    >>> ozify("How ya going?")
    'How ya going, eh?'
    """
    if not phrase[-1].isalpha():
        phrase = phrase[:-1]
    return phrase + ", eh?"


print(ozify("How ya going?"))
doctest.testmod()
