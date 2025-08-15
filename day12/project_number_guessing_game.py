# number_guess game
# https://pythontutor.com/visualize.html#mode=edit


import random

print("Welcome to the number guessing game")
print("i am thinking of  numbers between 1 and 100")

level = input("choose difficulty . Type easy or hard : ")
guess = int(input("make a guess : "))
choice = random.randint(1,100)


# def easy():
#     number_of_attempts = 5
#     for i in range(number_of_attempts):
#         print(f"you have {number_of_attempts} attempts remaining to guess the number")
#         guess
#         number_of_attempts -= 1
#         if choice < guess:
#             print("too low")
#         elif choice > guess:
#             print("too high")
#         elif choice == guess:
#             print(f"thats the correct number {guess}")
#         elif number_of_attempts < 1:
#             guess
#     if number_of_attempts < 1:
        
#         print("you dont have any left options") 

def easy():
    number_of_attempts = 5
    while number_of_attempts > 0:
        print(f"you have {number_of_attempts} attempts remaining to guess the number")
        guess = int(input("make a guess : "))
        if choice < guess:
            print("too high")
        elif choice > guess:
            print("too low")
        elif choice == guess:
            print(f"thats the correct number {guess}")
            return
        number_of_attempts -= 1
    print("you dont have any left options")
    print(f"the correct number was {choice}")


if level == "easy":
    easy()
# elif level == "hard":
#     hard()

