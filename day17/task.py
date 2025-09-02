class ndiwakar:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"new object created with name {self.name} and age {self.age}")

user1 = ndiwakar("ndiwakar", 30)
print(user1.name)
print(user1.age)

# fetching dictionary of the object
print(user1.__dict__)
print(type(user1))

# class is a blueprint of the object, and object is an instance of the class ... and method is a function inside the class with self parameter ... and attribute is a variable inside the class

print(dir(user1))

