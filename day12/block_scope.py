# there is no block scipe in python 

# https://www.w3schools.com/python/python_scope.asp

# https://docs.python.org/3/reference/executionmodel.html

# https://www.w3schools.com/programming/prog_scope.php

# todo : All the varaibles listed with in  blocks of the code example :  for, while , if statement basically dont get local scope , they are give function scope if they are in fucntion ....or global scope if they are not.

game_level = 10

enemies  = ["skeleton", "zombie","alien"]

def create_enemy():
    new_enemy = "" 
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)