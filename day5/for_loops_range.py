# range function with the loop
# and u want step by 3 places each time we can use this (1, 10, 3)

for number in range(1, 10, 3):
    print(number)


# adding numbers from 1 to 100
# it just iterating over the values from total value of 0 , and that becames 0 + 1 ,2+1,3+3,6+4...

total = 0
for num in range(1, 101):
    total += num
print(total)