#https://docs.python.org/3/library/random.html

import random

#creating the own module
import create_own_module

random_int = random.randint( 0, 1)

print(random_int)

print(create_own_module.my_favourite_number)

# to create random floating point numbers ... below we have added 10 where i give the results of 0 to 10 not  including 10
#https://docs.python.org/3/library/random.html#real-valued-distributions

random_number_0_to_1 = random.random() * 10

print(random_number_0_to_1)

random_uniform = random.uniform(1,10)
print(random_uniform)


# printing out the heads or tails based on the number we get from the random values

if random_number_0_to_1 <= 5:
    print("Heads")
else:
    print("Tails")


# or we can use randint function to do the same

if random_int == 1:
    print("Heads")
else:
    print("Tails")
