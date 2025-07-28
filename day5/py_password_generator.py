# password generator 
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
# here based on the user input , we need to randomly pick them and add them to list
# concatenate them into single using print
# k is used to specify the number of elements to be picked from the list
# i need to randomly pick letters, symbols and numbers based on the user input

#The join() method is called on an empty string '', which serves as the separator between elements. Since the separator is empty, the characters are concatenated directly without any spaces, commas, or other characters between them. The method takes final_password (which at this point should be a list or iterable of individual characters) as its argument


rand_letters = random.choices(letters, k=nr_letters)
rand_symbols = random.choices(symbols, k=nr_symbols)
rand_numbers = random.choices(numbers, k=nr_numbers)


final_password = rand_letters + rand_symbols + rand_numbers
# we need to shuffle the final password to make it more random
random.shuffle(final_password)
# join the list to make it a string
final_password = ''.join(final_password)
print("Here is your password ", final_password)

# there are two versions  of the generator one is just randomly pick the letters , number, sym.. and just concentate them
# second is to shuffle the final output using random,shuffle 