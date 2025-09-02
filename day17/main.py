# here we are creating the class and leave it as pass
# and all the classes are pascalcase {CarCamshaftPulley}
# PascalCase - every word starts with the capital(class)\
# camelCase - Every subsequent word is capital()

# snake_case - pretty much to name everything 



# class User:
#     def __init__(self):
#         print("new value getting created")

# print("hello")

# # we create new object from that claass below

# user_1 = User()

# # how to access/ add the attribute to that class

# user_1.id = "001"
# user_1.username = "ndiwakar"
# # when we print that particular attribute with the object getting displayed
# # and here attribute is a varibale with some value to it, we have alots of it
# print(f"{user_1.id}")

# in python we can use the constructors to initialize the attributes like below
# class Car:
# def __init__(self):
# initialise attributes
# with this it got triggered when we create the object everytime for every new object
# and we can also pass the parameters to the constructor

#https://www.geeksforgeeks.org/python/__init__-in-python/

#Effective way 
# we are deefaulting the followers to 0 if not passed


class User:
    def __init__(self, user_id, username, followers = 0):
        self.id = user_id
        self.username = username
        self.followers = followers

user_1 = User("001", "ndiwakar")
user_2 = User("002", "testuser")
print(user_1.id)
print(user_2.username)
print(user_1.followers)

# Adding a method to the class

# when function is inside the class it is called method
# and we need to pass the self parameter to the method
# self is the instance of the class
# and we can access the attributes of the class with self.attribute_name

class Car:
    def __init__(self, seats, color, mileage):
        self.seats = seats
        self.color = color
        self.mileage = mileage
        self.is_driving = False

    def drive(self):
        self.is_driving = True

    def stop(self):
        self.is_driving = False

    def get_status(self):
        if self.is_driving:
            return "The car is driving"
        else:
            return "The car is stopped"
        
my_car = Car(4, "red", 10000)
print(my_car.get_status()) # The car is stopped
my_car.drive() 
print(my_car.get_status()) # The car is driving
my_car.stop()
print(my_car.get_status()) # The car is stopped
