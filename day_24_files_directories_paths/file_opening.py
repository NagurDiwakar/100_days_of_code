file = open("my_file.txt") # open the file

contents = file.read() # reads the file

print(contents)

file.close() # close the file

# using 'with' automatically closes the file after the block
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# writing to a file
with open("my_file.txt", mode="w") as file:
    file.write("New text.")
    


# appending to a file
with open("my_file.txt", mode="a") as file:
    file.write("\nAppended text.")
    

# reading a file line by line
with open("my_file.txt") as file:
    for line in file:
        print(line)