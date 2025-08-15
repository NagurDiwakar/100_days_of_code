# given a list of numbers , list out the only even numbers

list = [1,2,3,4,5,6,7,8,9,10]

even_number_list = []

for i in range(len(list)):
    if i % 2 == 0:
        even_number_list.append(i)
    
print(even_number_list)