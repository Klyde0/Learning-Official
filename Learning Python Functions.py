# def hello_func():
#     print('Hello function.')

# pass basically allows you to put a placeholder for a undefined function

# functions are useful to put code in specific locations/instances over multiple lines
# this allows you to keep your code 'dry' = not repeating yourself
# allows you to make changes wherever that function is in your code

# return = when we execute our function, it will be equal to our return value
# these executed functions will be equal to our function
# an executed function is equal to the RETURN value
# can take executed function as whatever type it is returned as ie. in this case, a string

# def hello_func():
#     return('Hello function.')
#
# print(hello_func().upper())

# Passing arguments into functions

# def hello_func(greeting, name = 'You'):
#     return('{}, {}'.format(greeting, name))
#
# print(hello_func('Hi', name = 'Brian' ))

def hello_func(greeting, name = 'You'):
    return(f'{greeting}, {name}')

print(hello_func('Hi', 'Brian' ))
#
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# student_info('Math', 'Art', name = 'John', age = 22)

def cube(num):
    return num*num*num
result = cube(4)
print(result)


