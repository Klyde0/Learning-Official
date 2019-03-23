student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}\

# print(student['courses'])
# print(student['name'])
# print(student.get('name'))

# dictionaries have a "get" method - get can be used or just []
student['phone'] = '555-5555'

# print(student.get('phone', 'Not Found'))

# get methods in dictionaries can also have 2 arguments - in a variable that has keys,
# if the key you are trying to 'get' is not in there, you can place argument 2 to output 'Not Found'

# .update is another useful method when you want to update multiple keys in a dictionary
# .update takes in another dictionary in its method

student.update({'table': 'welcome', 'name': 'Jane', 'age': '26', 'phone': '23232-2323'})
# print(student)
# del is a method that deletes keys in dictionaries
# pop is a method that deletes removed last value but also returns it

# del student['age']
# print(student)

age = student.pop('age')
print(age)

print(student.keys())
print(student.values())

# .keys is a method that returns the keys in a dictionary
# .values is a method that returns the values of the keys in a dictionary

print(student.items())

# .items is a method that returns the keys and values of a dictionary

for key, value in student.items():
    print(key, value)

# in this for loop, the student.items() method will iterate through the key and value of the dict.

