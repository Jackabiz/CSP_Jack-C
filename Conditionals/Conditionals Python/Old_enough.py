#Jackson Clark, Old Enough Python
age = int(input("how old are you? \n"))


if (age>=18):
    print("you can go to school, drive, and even vote!")
elif (age >= 16 & age < 18):
    print("you can go to school and drive!")
elif (age >= 15.5 & age < 16):
    print("you can go to school and get your learner's permit!")
elif (age >= 5 & age < 15.5):
    print("you can go to school!")
else:
 print("how are you even using this program?")