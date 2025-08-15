# project calculator.py
# standard calculator implementation with functions for each operation

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print("Welcome to the Calculator!")
    
    num1 = float(input("Enter your first number: "))
    
    while True:
        for symbol in operations:
            print(symbol)
        
        operation_symbol = input("Pick an operation: ")
        
        if operation_symbol not in operations:
            print("Invalid operation. Please try again.")
            continue
            
        num2 = float(input("Enter your next number: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        should_continue = input("Type 'y' to continue calculating with the result, 'n' to start a new calculation, or 'q' to quit: ").lower()
        
        if should_continue == 'y':
            num1 = answer
        elif should_continue == 'n':
            calculator()  # Start fresh
            break
        elif should_continue == 'q':
            print("Thanks for using the calculator!")
            break
        else:
            print("Invalid input. Please try again.")

# Start the calculator
calculator()


