# calculator app 

# https://stackoverflow.com/questions/8347048/how-to-convert-string-to-title-case-in-python

#str.title in python

myname = "ndiwakar"

print(myname.title())

# output will  be Ndiwakar

#functions with outputs

def format_name(f_name,l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
formatted_string = format_name("nagur","diwakar")

print(formatted_string)


# difference between return and print statement
# in below we are inputting the one function output into another

def function_1(text):
    return text + text

function_1("hello")

def function_2(text):
    return text.title()

output =  function_2(function_1("hello"))
print(output)


