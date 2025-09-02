# how to create the class in python

class is a just a blueprint , here we are trying to create the own class that is own object

https://www.geeksforgeeks.org/python/__init__-in-python/

In Python, __init__ is a special method, often referred to as a "constructor," that is automatically called when a new instance (object) of a class is created. Its primary purpose is to initialize the attributes (variables) of the newly created object. 
Here's a breakdown of its key aspects: 

• Automatic Invocation: Unlike regular methods, you don't explicitly call __init__. When you create an object from a class (e.g., my_object = MyClass()), Python automatically executes the __init__ method defined within MyClass. 
• Initialization of Attributes: The __init__ method is where you typically assign initial values to the object's attributes. These attributes define the state of the object. 
• self Parameter: The first parameter of __init__ (and all instance methods) is conventionally named self. This self refers to the instance of the class being created, allowing you to access and modify its attributes within the method. 
• Accepting Arguments: __init__ can accept additional arguments beyond self, which are used to provide initial values for the object's attributes during its creation. 

Example: 
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Initialize the 'name' attribute
        self.breed = breed  # Initialize the 'breed' attribute

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador")

# Accessing attributes and calling methods
print(f"{dog1.name} is a {dog1.breed}.")
dog1.bark()

print(f"{dog2.name} is a {dog2.breed}.")
dog2.bark()

In this example, __init__ is used to set the name and breed of each Dog object when it's created. 



https://opentdb.com/


