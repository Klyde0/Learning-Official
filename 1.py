price_of_house = 1000000
#
# good_credit = False
#
# if good_credit:
#     down_payment = 0.1 * 1000000
#     print('Put down ' + str(down_payment))
#
# else:
#     down_payment = 0.2 * 1000000
#     print('Put down ' + str(down_payment))


# good_credit = False
#
# if good_credit:
#     down_payment = 0.1 * price_of_house
#
# else:
#     down_payment = 0.2 * price_of_house
#
# print(f'Please put down {down_payment}')

# temp = 20
#
# if temp > 30:
#     print('Its a hot day')
#
# elif temp < 10:
#     print('Its a cold day')
#
# else:
#     print('Its neither hot nor cold')

user_input = input('Please type in your name:')

if len(user_input) < 3:
    print('name must be at least 3 characters')

elif len(user_input) > 10:
    print('name can be max 10 characters')
else:
    print('name looks good')