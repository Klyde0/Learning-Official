greeting = 'Hello'
name = 'Brian'

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# FStrings = make formatting strings much easier (only available on Python > 3.6

course = 'Python for Beginners'
# course = course[:6] + "'s Guide to Python" + course[6:]

print(course)

# How to add specific things to strings - update the variable containing the string
# Can also replace things in Strings using .replace method

print(course.replace('Python', "Brian's Guide to Python"))

course = 'Python for Beginners'
course = course[:6] + "'s Guide to Python" + course[6:]

print(course)