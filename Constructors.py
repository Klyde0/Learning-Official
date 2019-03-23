# Constructors = function that gets called at the time of creating an object
#       __init__(self) = constructor
#       This is the function/method that gets called when we initialize a new object
#       After (self, value1, value2), the values are used to initialize the object
# 'self' represents the instance of the class. By using the self keyword, we can access attributes and methods of the class and have it apply to the object


class Point:
    def __init__(self, x, y):
        self.candy = x
        self.toys = y
    # self is a reference to to the current object
    # self.x = x (x attribute is set to x argument of the function)
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1= Point(10, 20)
# Here the object is created, so when we pass arguments into Point()
# 10 and 20 are used to initialize the object point1 for x and y parameters

print(point1.candy)
# this will print out 10 because 10 was the argument given in the x position of the Class
# self initializes point1 as the object and because self.candy (object.attribute) = x, and we gave 10 as the argument for x
# we will print out 10 when we call print1.candy
#