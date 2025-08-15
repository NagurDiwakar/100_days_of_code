# functions with inputs
# Arguments and parameters

# cipher - each letter is shifted by the pre-determined amount
# lets say a,b,c,d shifted by the 4 places than it becames a->d,b->e,...

#function is basically is just add all the code under that , when ever need we can just call the function() by followed parantheses in the program

def greet():
    print("Hello")
    print("How are you")
    print("isn't the weather beautiful ?")

greet()

# even after multiple calls it prints same , it print diff dynamincally or print by someone's name thats where the whole difference came in with diff parameters each time

#def func (something) to execute

def greet_with_name(name):
    print(f"hello {name}")
    print("how are you ")
    print("isn't the weather nice? ")

greet_with_name("ndiwakar")


# when we are passing the input to the function lets say  in above name is parameter and ndiwakar is argument 

