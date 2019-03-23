
print('Imported module')

test = 'Test String'

def find_index(list, target_index):
    for i, value in enumerate(list):
        if value == target_index:
            return i
    return -1


# L = ['apples', 'bananas', 'oranges']
# for i, value in enumerate(L):
#   print(f'index is {i} and value is {value}')