# for x in range(4):
#     for y in range(3):
#         print(f'({x} , {y})')

# for x, y in range(5):
#     x += 1
#     y += 1
#     print(f'{x},{y}')


numbers = [5, 2, 5, 2, 2]

for x in numbers:
    output = ''
    for count in range(x):
        output += 'x'
    print(output)