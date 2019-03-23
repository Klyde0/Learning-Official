def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# *args and **kwargs allows us to accept a number of positional/keyword arguments
# *args / **kwargs= when we dont know how many keyword positional arguments there will be, we use *args and **kwargs
#  according to standard Python convention - doesnt need to be args/kwargs
# *args = list (positional argument)
# **kwargs = dictionary (keyword argument)
# the * unpacks the values and passes them in individually

courses = ['Math', 'Art', 'Calculus', 'Physics']
info = {'name': 'John', 'age': '20', 'height': "5'11"}
student_info(*courses, **info)
