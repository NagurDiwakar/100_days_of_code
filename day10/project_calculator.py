# project calculator.py
output = 0

def calculator(first_calculation=True):
    global output
    
    if first_calculation:
        number_1 = int(input("enter ur first number : "))
    else:
        number_1 = output
        print(f"Your current result is: {number_1}")
    
    operation = input("pick the operation +,-,*,/ : ")
    number_2 = int(input("enter ur next number : "))
    
    if operation == '+':
        output = number_1 + number_2
        print(f"{number_1} + {number_2} = {output}")      
    elif operation == '-':
        output = number_1 - number_2
        print(f"{number_1} - {number_2} = {output}") 
    elif operation == '*':
        output = number_1 * number_2
        print(f"{number_1} * {number_2} = {output}") 
    elif operation == '/':
        output = number_1 / number_2
        print(f"{number_1} / {number_2} = {output}") 
    else:
        print("invalid operation input from the user")
        
    return output


# with this function again we are using again performing the second time  input 1


def continue_calculation():
    continue_calc = input("Type Y to continue to calculate with previous output or type n to start a new calculation: ").lower()
    if continue_calc == 'y':
        calculator(first_calculation=False)
        continue_calculation()
    elif continue_calc == 'n':
        calculator(first_calculation=True)
        continue_calculation()
    else:
        print("Invalid input. Please try again.")
        continue_calculation()

# Start the calculator
calculator(first_calculation=True)
continue_calculation()


