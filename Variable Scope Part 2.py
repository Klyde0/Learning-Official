# def test(z):
#     x = 'local x'
#     print(z)
#
# test('local z')
# In this scenario, 'local z' string is defined in the local scope of the test function, hence it prints out local z
# print(x)

# built-in functions are already built into Python

# import builtins
# print(dir(builtins))
#
# m = min([5,1,4,2,3])
# print(m)

# here we were able to use min because its a built-in function in Python
# we can import builtins
# then we can just print out dir on built-ins which give the attributes of the given object
# BE CAREFUL NOT TO ACCIDENTALLY OVERWRITE BUILTINS

import builtins

# def my_min(m):
#     pass
#
# m = min([5,1,4,2,3])
# print(m)
# TypeError: min() takes 0 positional arguments but 1 was given
# the reason for this error was that Python found min in the global scope before it fell into the local scope

# ENCLOSING SCOPE - has to do with nested functions

x = 'global x'
def outer():
    x = 'outer x'

    def inner():
        # nonlocal x
        # nonlocal x - this will allow us to work with local variables of ENCLOSING FUNCTIONS - we're now affecting the x variable of the outer function
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()
print(x)