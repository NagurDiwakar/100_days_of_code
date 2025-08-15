# set the lives for the guess , declaring a variable with some value , upon completing the guess we need to look for new


stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

list = ['answer','baboon','artisan']

random_word = random.choice(list)

print(random_word)


#placeholder
placeholder = ""
for position in range(len(random_word)):
    placeholder += "_"
print(placeholder)


lives = 6
game_over = False
correct_letters =[]
while not game_over :
    user_input = input("Guess a  letter :").lower()

    display = ""
    for letter in random_word:
        if letter == user_input:
            display += letter
            correct_letters.append(letter) #or user_input is also fine since they both are same 
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    if user_input not in letter:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose ")
        
    print(display)
    if "_" not in display:
        game_over = True
        print("you win.")
    
    print(stages[lives])