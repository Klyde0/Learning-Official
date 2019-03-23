# How to handle errors
# Try/Except lines will allow your program to try something and tell you what types of errors you made without breaking your program
# ex. for example if you enter a string instead of a number


try:
    answer = 10/0
    number = int(input('Enter a number: '))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print('Invalid Input')

# In this example, we wrote multiple except lines with 2 different types of potential errors in our code
#