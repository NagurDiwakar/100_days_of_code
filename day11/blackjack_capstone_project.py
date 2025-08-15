#https://appbrewery.github.io/python-day11-demo/
# black jack game has threshold of 21 in the start the two cards are ginven with some values if those added or nearer to 21 and computer or 
# dealer is very close to threshold than obviously added up to winiing 

# whover close to 21 wins
# if ur second or third card either from the user or computer is more than 21 , those will lose the game immediately

# for computer we should have set some value first inbetween 1-15 , using random for second value if those acculumated is nearer and greater than 21 computer wins or user wins
# for user also we use random for initial values and input the remaining values
# to continyue by prompt from user until prompt n , yes for continue the game -- while loop done the functionality
# for user has multiple values consider declaring a list with two values adding them to single value and it should be less than 21
# and similar computer has some value after ur pick , it should go over remaining values adding compare it with user values
# if the total is less than 17 than automatically one choice is left to work upon

# the cards in the below list has equal probability of being drawn
#jack/queen/king all counted as 10
# ace can be counted as either 1 or 11

from itertools import count
import random

list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user =[]
computer = []
new_value = ""


user = random.choices(list, k=2)
computer = random.choices(list, k=2)
count_user = sum(user)
count_computer = sum(computer)
print(f"user", user ,"=" ,{count_user})
print(f"computer", computer, "=" ,{count_computer})

magic_number_to_win  = 21

def if_values(user,computer):
    user_input = input("enter Y for select for another card : ").lower()
    if user or computer < 17:
        if user_input == "y":
            new_value = random.choices(list)
            print(f"your card value is {new_value}")
            user.append(new_value)
            print(user)
            blackjack()
    else:
        blackjack()





def blackjack():
    if count(user) > count(computer):
        print(f"user wins with score {user}")
    else:
        print(f"computer wins with score {computer}")


if_values(user,computer)
blackjack()


