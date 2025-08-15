# number guessing game
# TODO: namespaces local vs global scope
# global scope 

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function : {enemies}")

increase_enemies()


print(f"enemies outside function : {enemies}")


# local scope

def drink_portion():
    portion_strength = 2
    print(portion_strength)

drink_portion()

# which will output the error becos those value is local scoped
#print(portion_strength)

# for global scope is  having above example

# todo:  this is not only applies to teh variables , this applies to the functions too , "THIS CONCEPT IS CALLED NAMESPACES" 

# NEED TO CHECK FUNCTION OF FUNCTION SCOPES
# def 1():
#    def 2():
#.    variable name
#    call function()


# TODO:  " DOES PYTHON HAVE BLOCKSCOPE "


