# Here the task is to pick one of them to pay the bill for which we are using the random and lists to do the task

import random

list_of_persons = ["lakshmi", "dinesh", "chiru", "gnana", "kumar", "diwakar"]

random_picking = random.choice(list_of_persons)

print(random_picking)


#2nd option
#to print out the list make sure use the [ ] in the lists

random_index = random.randint(0, 5)
print(list_of_persons[random_index])