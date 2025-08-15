# replacing with blanks instead of letters

import random

list = ['ant','bag','cat']

random_word = random.choice(list)

print(random_word)


#placeholder
placeholder = ""
for position in range(len(random_word)):
    placeholder += "_"
print(placeholder)

# lives = ""

# # while lives in range(1,7):
# user_input = input("Guess a  letter :").lower()

# display = ""


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
    print(display)
    if "_" not in display:
        game_over = True
        print("you win.")
