# Parameters allow you to pass information into your functions
# argument = value supplied to a function
# parameters = placeholders of arguments in functions
def greet_user(firstname):
    print(f'Hi there {firstname}')
    print(f'Welcome aboard {firstname}!')


print('Start')
greet_user(5)
print('Finish')


# keyword argument = argument followed by keyword
# ex. greet_user ('Smith', first_name = John) - first_name = 'John' is a keyword argument
# Keyword arguments must always come after positional arguments
