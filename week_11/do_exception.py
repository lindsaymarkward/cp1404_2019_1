
"""

boolean
while boolean
try
except

print age odd/even

"""

is_valid_age = False
while not is_valid_age:
    try:
        age = int(input("Age: "))
        if age < 0 or age > 120:
            print("Error")
        else:
            break
    except ValueError:
        print("Error")

if age % 2 == 0:
    print("Even")
else:
    print("Odd")
