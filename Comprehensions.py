nums = [1,2,3,4,5,6,7,8,9,10]

# For Loops comprehension

# I want 'n' for each 'n' in nums
# my_list = []
# for n in nums:
#   my_list.append(n)
# print (my_list)
#
# print ([n for n in nums])

# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
#   my_list.append(n*n)
# print(my_list)

# print([n*n for n in nums])

# For Loops Comprehension with integer operations

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#   if n%2 == 0:
#     my_list.append(n)
# print my_list

# my_list = [n for n in nums if n%2 == 0]
# print(my_list)



# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
#
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# my_list = []
# for letter in 'abcd':
#   for num in range(4):
#     my_list.append((letter,num))
# print my_list

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

result = zip(names, heros)
result_list = list(result)
# zip function basically matches up the first element of each list with one another
print(result_list)

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)
# If name not equal to Peter

# Sets are basically lists of unique numbers only - expressed using {} THEY CANNOT BE INDEXED BECAUSE THEY ARE UNORDERED
# Set Comprehensions
# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print (my_set)

# my_set = {n for n in nums}
# print(my_set)

# Generator Expressions - use ()
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n
#
# my_gen = gen_func(nums)
#
# for i in my_gen:
#     print(i)
#
# my_gen = (n*n for n in nums)
#
#
# for i in my_gen:
#     print(i)
