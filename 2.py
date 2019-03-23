# i = 1
#
# while i <= 5:
#     print('Hello' * i)
#     # you can have strings be multiplied
#     i += 1
# print('done')


guess_counter = 0
guess_limit = 3
secret_number = 12


while guess_counter < guess_limit:
    guess = int(input('Take a guess: '))
    guess_counter += 1
    if guess == secret_number:
        print('You are correct!')
        break

else:
    print('Sorry, you are out of guesses.')

