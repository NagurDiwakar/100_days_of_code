https://www.w3schools.com/python/python_classes.asp

Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

The __init__() Method
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() method.

All classes have a method called __init__(), which is always executed when the class is being initiated.

Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created:


Create a class named Person, use the __init__() method to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

The __str__() Method
The __str__() method controls what should be returned when the class object is represented as a string.

If the __str__() method is not set, the string representation of the object is returned:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

