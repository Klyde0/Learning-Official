nums = [1, 2, 3, 4, 5]

# for num in nums:
#     if num == 3:
#         print('Found it!')
#         break
#     print(num)


# the for loop causes the interpreter to spit out the first element in the list, then iterates to the next
# element in the list, and so on until it reaches the end of the list
# break = completely break out of loop - say you are looping through a list and you find the element you want
# attaching a break in your for loop will cause you to break out of the loop once you found what you want
# continue = move on to the next iteration of the loop. Ex. say you wanted to ignore a value in a list and just continue on with the loop


# for num in nums:
#     if num == 3:
#         print('Found it!')
#         continue
#     print(num)


# LOOPS WITHIN LOOPS - in the below example, the loop will iterate through the numbers, as well as the letter
# in the string 'abcd = gives us every combinations (be careful with nested loops)

# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

# Lets say we want to go through a loop a certain number of times = range (function)
# The range function does not include the last element in the range

for i in range(1, 11):
    print(i)
    