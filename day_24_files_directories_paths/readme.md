How to read , open ,write to the files using the "with" keyword and open file .. "open"is used

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

file = open("my_file.txt") # open the file

contents = file.read() # reads the file

print(contents)

file.close()

# we need to ensure to close the file , becos it takes the resources from ur computer or file

# with the above processs we might be missing out close the file , the effective way is to use "with" keyword

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
# with keyword automatically closes the file after the indented block is executed

# by default we open the file in read mode "r" , we can also open the file in write mode "w" or append mode "a"

with open("my_file.txt", mode="w") as file:
    file.write("New text.")  # this will overwrite the existing content

with open("my_file.txt", mode="a") as file:
    file.write("\nAppended text.")  # this will add to the existing content
# we can also read line by line using readline() or readlines()
with open("my_file.txt") as file:
    for line in file:
        print(line.strip())  # strip() removes extra newlines
# or
with open("my_file.txt") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip()) to handle files effectively.



# when you are trying to write to a file that does not exist , python will create that file for you (ONLY WORKS IN WRITE OR APPEND MODE)

# example:
with open("new_file.txt", mode="w") as file:
    file.write("This is a newly created file.")


#understanding file paths
# when you provide just the file name like "my_file.txt" , python looks for that file in the current working directory
# you can also provide absolute or relative paths to open files located elsewhere on your system

# example of absolute path
with open("/Users/username/Documents/my_file.txt") as file:
    contents = file.read()
    print(contents)
# example of relative path
with open("../other_folder/my_file.txt") as file:
    contents = file.read()
    print(contents) 
# this goes one directory up and then into other_folder to find my_file.txt 

# exact difference between absolute and relative paths can be found here
https://docs.python.org/3/library/os.path.html#os.path.abspath

# "Absolute paths always start from the root directory, while relative paths are based on the current working directory".


# for the  files which are in the same directory we can use  "filename.txt" if they are in different directory we can use relative or absolute path ( a directory above where you are working we can use ../directory_name/filename.txt  which is relative path ---- for absolute path we can use /users/username/directory_name/filename.txt )

# Absolute file path vs Relative file path -  afp is always starting from root directory whereas rfp is starting from current working directory


readlines() - reads all the lines of a file and returns them as a list of strings
readline() - reads a single line from a file each time it is called

strip() - removes any leading and trailing whitespace characters (including newlines) from a string
replace() - replaces occurrences of a specified substring with another substring in a string

example usage of strip() and replace():
with open("my_file.txt") as file:
    contents = file.read()
    cleaned_contents = contents.strip().replace("old_text", "new_text")
    print(cleaned_contents)

# Summary:
# Use "with open()" to handle files safely and automatically close them.
# Use mode="r" for reading, mode="w" for writing (overwrites), and mode="a" for appending.
# Use absolute or relative paths to locate files outside the current directory.
# Use read(), readline(), or readlines() to read file contents as needed.       


# readlines example
with open("my_file.txt") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes extra newlines




