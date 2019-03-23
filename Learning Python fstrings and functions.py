

# def hello_func(greeting):
#     return '{} Function.'.format(greeting)
#
# print(hello_func('Hi'))
# default value specified in positional argument of function name = 'you'
def hello_func(greeting, hello, name = "you"):
    return f'{greeting} {hello}, I am the Hello Function. This is a {name}'

print(hello_func('Hello', 'Brian', 'John'))