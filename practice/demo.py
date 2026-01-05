lst = [1, 2, 2, 3, 4, 4, 5]
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates(lst))

# here set() is used to remove duplicates from the list by converting it to a set and then back to a list.

# we can use list comprehension or loop to achieve the same result without using set()

def remove_duplicates_no_set(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

print(remove_duplicates_no_set(lst))

# list comprehension version

def remove_duplicates_list_comp(lst):
    unique_lst = []
    [unique_lst.append(item) for item in lst if item not in unique_lst]
    return unique_lst
print(remove_duplicates_list_comp(lst))

# fibonacci sequence without using recursion
# fibonacci series means each number is the sum of the two preceding ones, usually starting with 0 and 1. for example, the sequence goes like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# in below 10 as input will give 55 as output because 55 is the 10th number in the fibonacci series starting from 0.
# 0 , 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))  # Output: 55

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(fibonacci_iterative(10))  # Output: 55

# multithreading example in python
# multithreading is a technique where multiple threads are spawned by a process to do different tasks concurrently within the same program.

import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in 'abcde':
        print(letter)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start() # it starts the thread t1 , then t2 starts ... here start() method is used to start the thread 
t2.start()

t1.join() # join() method is used to wait for the thread to complete its execution before moving on to the next line of code
t2.join()


# sorting the dictionary by values
d = {'apple': 15, 'banana': 10, 'cherry': 20}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1])) # here it uses sorted() function to sort the dictionary items based on their values 10 ,15,20
print(sorted_d)  # Output: {'banana': 10, 'apple': 15, 'cherry': 20}


# sorting the list of numbers based on value 

lst_numbers = [5, 2, 9, 1, 5, 6]
sorted_lst = sorted(lst_numbers) # it uses sorted() function to sort the list in ascending order
print(sorted_lst)  # Output: [1, 2, 5, 5, 6, 9]

# or we can use list.sort() method to sort the list in place
lst_numbers.sort()
print(lst_numbers)  # Output: [1, 2, 5, 5, 6, 9]

# or sorting them using loop

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        # it arranges the largest element at the end of the list in each iteration
        for j in range(0, n-i-1): 
            # inner loop for comparing adjacent elements up to n-i-1 (n-i-1 because last i elements are already sorted)
            # here n-i-1 is used to avoid checking the already sorted elements at the end of the list 
            # compare adjacent elements , example if first is greater than second then swap them 
            # first iteration : 5,2 -> 2,5 ; 9,1 -> 1,9 ; 5,6 -> 5,6
            # the whole flow is like below
            # 5,2,9,1,5,6 [initial]
            # 2,5,9,1,5,6  [after first swap using first two elements]
            # 2,5,1,9,5,6  [after second swap using next two elements]
            # 2,5,1,5,9,6 [after third swap using next two elements]
            # 2,5,1,5,6,9   [after fourth swap using next two elements]
            # 2,1,5,5,6,9 [after first swap of second iteration]
            # 1,2,5,5,6,9  [after second swap of second iteration]

            if lst[j] > lst[j+1]: # if first element is greater than second element then swap them , if not then do nothing
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(bubble_sort(lst_numbers))  # Output: [1, 2, 5, 5, 6, 9]

