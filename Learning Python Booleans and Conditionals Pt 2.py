# a = [1, 2, 3]
# b = [1, 2, 3]
# # b = a
# print(a == b)

# # print(a is b) will return False because a and b are 2 different objects stored in computer memory
# # can print out locations in memory by using id()
# # is basically asks if id(a) == id(b)
# print(id(a))
# print(id(b))
# print(a is b)

# None = is a condition that evaluates to False
# 0 = is a condition that evaluates to False
# any number not 0 = is a condition that evaluates to True
# any empty sequence ex. '' , () , [] = will evaluate to False
# any empty mapping (ie. empty dictionary) ex. {} = will evaluate to False
# This is useful to know because lets say you have a function or something that is supposed to return
# some values. you might want to check if the string/dictionary etc. is empty
# so you pass in a empty string, dictionary, etc.

condition = 'fdsjaio'
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

