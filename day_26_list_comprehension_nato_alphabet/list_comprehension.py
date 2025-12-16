# to double the numbers

numbers = range(1,5)

number = [ n * 2 for n in numbers]

print(number)

# caping the listed names 
# https://www.geeksforgeeks.org/python/isupper-islower-lower-upper-python-applications/

names  = ["Bhavishya" , "Gayathri" , "Diwakar", "Tara"]

cap_names = [name.upper() for name in names if len(name) > 3]

print(cap_names)