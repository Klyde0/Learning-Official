names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mark']

# list = [1, 31, 5, 161]
# max = max(list)
#
# print(f'{max}')

numbers = [1, 31, 5, 12]
max = numbers[0]

for number in numbers:
  if number > max:
    max = number
print(max)