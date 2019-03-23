# You can take a string ex. phrase or a word and translate it into another language

# In our Python language Translator
# vowels -> g
# ex. dog -> dgg
# ex. cat -> cgt

def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation +'G'
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate(input('Enter a phrase: ')))