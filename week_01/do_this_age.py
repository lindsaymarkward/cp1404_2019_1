"""
get age
if age >= 18
    print adult
else
    print child
"""
AGE_OF_MAJORITY = 21

age = int(input("Age: "))
if age >= AGE_OF_MAJORITY:
    print("Adult")
elif age < AGE_OF_MAJORITY:
    print("Child")
