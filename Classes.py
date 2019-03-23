# Use Classes to define new types of data (anything not Numbers, Strings, Booleans, Lists, Dictionaries)

# start by class followed by the name of the class
# naming convention dictates that you Capitalize Class names - Pascal naming convention
# variables and functions are undercase
# after you define the class, name all the functions and methods inside the class - automatically adds self
# after you define your class with functions/methods, name Object
# an object = instance of a class
# object = Class() - this will make object as an instance of the Class


class Point:
    def move(self):
        print('move')
    def draw(self):
        print('draw')


point1 = Point()
point1.draw()

point1.x = 10
point1.y = 20
# OBJECTS CAN HAVE ATTRIBUTES = VARIABLES ASSOCIATED WITH A PARTICULAR OBJECT
print(point1.y)

point2 = Point()
# print(point2.x)
    # This will return an Attribute error because point2.x is not defined as an attribute of object point2

