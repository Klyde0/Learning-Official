# In Python, you can work with different types of data (strings, numbers, Booleans)
# You can also sort these data with lists, dictionaries, tuples, etc.
# However not all things can be represented as strings, numbers, Booleans. ex. objects
# Classes allow us to create our own data types ex. create phone class, student class, computer class, etc,
# and attribute all types of values (strings, numbers, Booleans) related to the phone. \
# Each entry element that has such attributes is considered an 'object' of the class

# Lets say we want to make a 'student' class of data
# To do so, we create an initialized function =
# def __init__(self, string/int/Boolean, string/int/Boolean, string/int/Boolean, ... ):

class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation