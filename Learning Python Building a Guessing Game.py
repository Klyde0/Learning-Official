# User will store a secret word and user will keep guessing until word is found
# Here we use a while loop so that the prompt will continue to ask user for input until word is found

# secret_words = 'python'
# guess = ''
#
# print('Welcome to the guessing game.')
# input('Please take a guess: ')
# if guess == secret_words:
#     print('Correct')
# while guess != secret_words:
#     guess = input('Incorrect. Please take another guess: ')
# else:
#     print('You are correct!')

# Above is a simple guessing game I made
# Below is a more complex guessing game with a guess counter

secret_words = 'python'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_words and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input('Please take a guess: ')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print('Out of guesses. YOU LOSE')
else:
    print('You are correct!')






