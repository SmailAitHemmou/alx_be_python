  # Arithmetic Operations Function :

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2 if num2 != 0 else print("Cannot divide by zero.")
    else:
        print("Operation not recognized. Use 'add', 'subtract', 'multiply', or 'divide'.")
