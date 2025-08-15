#https://www.geeksforgeeks.org/python/python-docstrings/

# it defines what will ur modules, functions, classes, and methods will do kind of explaination what will ur function do ?
# example

def format_name(f_name,l_name):
    """take a first name and last name
    format it to the title case """ # doc string
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
formatted_string = format_name("nagur","diwakar")



