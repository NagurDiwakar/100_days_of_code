# with in this game , the input option should be from the user , computer is from the random module

# this is not robust program its not covering usecases if user enter other than 0-2 
# and also what will happens if he gives 234 -> out of range error
import random
print("Welcome to rock paper scissors game")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



options = [rock, paper, scissors]

try: 
     user_input = int(input("what do you chose TYPE 0 for rock , 1 for paper or 2 scissors \n"))
     if user_input < 0 or user_input > 2:
        print("Invalid input! Please enter a number between 0 and 2.")
        exit()
except ValueError:
    print("Invalid input! Please enter a valid integer between 0 and 2.")
    exit()


user_option = options[user_input]
print("you choose" , user_option)


computer_random_options = random.choice(options)
print("computer choose",computer_random_options)


#The winner is determined by the rules: rock crushes scissors, scissors cuts paper, and paper covers rock. 
# if the both option are same , than game will be tie


if user_option == computer_random_options:
    print("Game tie")
elif user_option == options[0] and computer_random_options == options[2]:
    print("you win, rock crushes scissors")
elif user_option == options[2] and computer_random_options == options[0]:
    print("computer win, rock crushes scissors")
elif user_option == options[2] and computer_random_options == options[1]:
    print("you win, scissor cuts papers")
elif user_option == options[1] and computer_random_options == options[2]:
    print("computer win, scissors cuts papers")
elif user_option == options[1] and computer_random_options == options[0]:
    print("you win, paper covers rock")
elif user_option == options[0] and computer_random_options == options[1]:
    print("computer win, paper covers rock")
else:
    print("Nobody wins")
