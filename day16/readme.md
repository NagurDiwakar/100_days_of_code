https://realpython.com/python3-object-oriented-programming/
https://docs.python.org/3/tutorial/classes.html
https://www.geeksforgeeks.org/python/accessing-attributes-methods-python/

attributes and methods define an object's behavior and encapsulate data within a class. Attributes represent the properties or characteristics of an object, while methods define the actions or behaviors that an object can perform

attribute - have the things 
method - can perform the data

constructing tghe objects AND accessing the attributes and methods

car color, funtionality,blueprint, brakes and stoppage -> class

from the car class we can generate many objects as we want

car = CarBlueprint()

car -> objetc
CarBlueprint() -> class

And that blueprint which models a real-life car is known as the class.

And it's from this blueprint,

this class, that we can generate as many objects as we want. Now,

the object is the actual thing that we're going to be using in our code.

The code equivalent of what just happened,

creating a new object from a blueprint,

looks like this in Python. You have the class

which is normally written with the first letter of each word capitalized,

which is known as Pascal case.

This is to differentiate it from all the variable and function names that we

give in Python, where each word is separated by underscores.

So in this case,

the car is the object and it gets created from this car blueprint.

All we have to do to create the object from the class is to give the object a

name, it can be anything you want, set it equal to the name of the class,

and then the parentheses, which in the same way as it activates the function,

Example : using the turtle module and fetching the Turtle class

https://docs.python.org/3/library/turtle.html
https://cs111.wellesley.edu/reference/colors

from turtle import Turtle

timmy = Turtle()

print(timmy)

as mentioned if we consider car as an object and its more attributes like speed,fuel etc

car -> object
speed,fuel -> attributes

to access the atribute car.speed -> identifyinng thge object abd get tghe vakye of the attribute

https://docs.python.org/3/library/turtle.html#turtle-methods

Package installation and search

https://pokemondb.net/pokedex/game/x-y
https://pypi.org/
https://pypi.org/project/prettytable/
https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki



modifying the object attributes and the calling methods

from prettytable import PrettyTable

table = PrettyTable()

print(table)


In OOP what is the name of the blueprint for creating objects?

class (The reason "Class" is correct is that it serves as the fundamental blueprint in Object-Oriented Programming (OOP) for creating and defining objects, encapsulating their attributes and behaviors. This essential concept helps you understand how objects are structured and instantiated in OOP.)

Given a Class blueprint for a Car has the following attributes and methods, which line of code in the answers will produce an error?

Attributes:

num_of_seats

speed

Methods:

drive()

brake()

For this answer is car.brake() brake is a metjhod , which means its functions associated with the car object which caNNOT Assign to the function call

my_toyota = Car()
my_fiat = Car()
What word would you use to describe what's inside my_toyota and my_fiat?

my_toyota and my_fiat are the variables and each contains the car object






