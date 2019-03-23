# Handling Errors
# Comments should explain Whys/Hows/Assumptions/Reminders
try:
    age = int(input('Age:'))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print('age cannot be 0')
# exit code 0 = code successfully completed
# exit code 1 = program crashed
# a good programmer wont let a program crash, instead he/she will build in a way to handle errors with exceptions

