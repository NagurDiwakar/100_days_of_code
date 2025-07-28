import random
print("Welcome to Py password Generator")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','&','*']
nr_letters = int(input("How many letters would you like in our password \n"))
nr_symbols = int(input("How many symbols would you like in our password \n"))
nr_numbers = int(input("How many numbers would you like in our password \n"))

print('''
''')

# password = " "

# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)


# print("your password ", password)


#hard level


password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")