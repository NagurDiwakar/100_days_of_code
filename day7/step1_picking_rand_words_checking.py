# randomly selection the word and select one of the them
#https://developers.google.com/edu/python/lists#for-and-in

# declare a list with a words and randomly choose a word in that list
# ask the user to guess a letter make it lowercase
# if that is particular letter is in the choose word , than print right or wrong

import random

list = ['ant','bag','cat']

random_word = random.choice(list)

print(random_word)

user_input = input("Guess a  letter :").lower()
print(user_input)


for letter in random_word:
    if letter == user_input:
        print("right")
    else:
        print("wrong")
     


