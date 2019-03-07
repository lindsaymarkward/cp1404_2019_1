
# <priming read - do something the loop will depend on, e.g. get/calculate a number>
# while <condition based on something from above>:
#     <body of the loop - do the thing you want to repeat>
#     <same as the priming read again>
# <do next thing now that the loop is finished (condition was false)>

# Here's our normal pattern - all good :)
# number = int(input("Age: "))
# while number > 0:
#     print(number ** 2)
#     number = int(input("Age: "))

# Problem pattern 1 - forcing the while to be true the first time
# Usually people do this to avoid the repeated priming read
# BUT, you need to repeat the condition, which is worse (inefficient)
# number = 90
# while number > 0:
#     number = int(input("Age: "))
#     if number > 0:
#         print(number ** 2)

# Problem pattern 1 - while True
# As the notes say, if you need an if to break out, that should just be your condition
# This code is harder to read because you need to search for the break to understand the loop
# while True:
#     number = int(input("Age: "))
#     if number <= 0:
#         break
#     else:
#         print(number ** 2)



total_age = 0
number_of_people = 0
age = int(input("Age: "))
while age >= 0:
    total_age += age
    number_of_people += 1
    age = int(input("Age: "))
print(total_age / number_of_people)
