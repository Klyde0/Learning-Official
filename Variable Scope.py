# Variable scope - what determines where our variables can be accessed from and what values those variables hold
# LEGB = Local, Enclosing, Global, Build-in
# Local -variables defined within a function
# Enclosing - variables in the local scope of enclosing functions
# Global - variables defined at the top level of a module or explicitly declared global using the global keyword
# Built-ins - names preassigned in Python

# LEGB is the order that determines what scope a variable is assigned to
# Say that you have a variable assigned global

x = 'global x'

def test():
    global x
    x = 'local x'
    # Here the y variable is a local variable that is local to this test() function
    # print(y)
    print(x)
test()
print(x)
# Python used the LEGB rule and checked if y was in the local scope which are variables defined within the function
# When we print(x), we print out global x, x was assigned a global scope because it wasnt in local, enclosed.

# print(y)
# NameError: name 'y' is not defined
# y variable doesnt live outside the test function. So because its not in the local, enclosing, global, or built-in scope
# so you get the NameError

# You really shouldnt be setting global scope variables
# Local scope variables are contained so you dont have to worry about them messing up different parts of your code
# Important for code maintenance
