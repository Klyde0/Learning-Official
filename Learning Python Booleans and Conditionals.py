# if True:
#     print('Conditional was True')
#
# # will print statement only if conditional was True
#
# if False:
#     print('Conditional was True')
#
#
# language = 'Python'
#
# if language == 'Python':
#     print('Conditional was True')

# Here the statement is printed because the conditional was true
# is = object identity = comparing whether they are the same object in identity

# language = 'Javascript'
# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# elif language == 'Javascript':
#     print('Language is Javascript')
# else:
#     print('No Match - language is different')

# typical conditional statements
# if --- elif --- elif --- ... --- else

# Booleans = and, or, not

# user = 'Admin'
# logged_in = False
#
# if user == 'Admin' and logged_in:
#     print('Admin Page')
# else:
#     print('Bad Credentials')
#
# user = 'Admin'
# logged_in = True
#
# if logged_in:
#     input('Please Log in:')
#
# elif logged_in == True:
#     print('Welcome')
# else:
#     print('Bad Credentials')

is_male = False
is_tall = False

if is_male and is_tall:
    print('You are a Male and Tall')
elif is_male and not is_tall:
    print('You are a short male')
elif not is_male and is_tall:
    print('You are not a male but you are tall')
else:
    print('You are not a male and not tall')