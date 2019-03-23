# prices = [10,20,30]
#
# total = 0
# for x in prices:
#     total += x
#
# print(f'Total: {total}')

for i in range(99, 0, -1):
    if i == 1:
        print(
"""1 more bottle of beer on the wall. 1 more bottle of beer!
So take it down, pass it around, 0 more bottles of beer on the wall!'
""")
    else:
        print(f'{i} bottles of beer on the wall, {i} bottles of beer!')
        print(f'So take it down, pass it around, {i-1} more bottles of beer on the wall!')