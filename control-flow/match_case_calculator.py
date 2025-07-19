# Simple Calculator with Match Case – No if/else used
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
input_operator = input("Choose the operation (+, -, *, /): ")
# Handle zero division in operator choice
if num2 == 0 and input_operator == '/':
    result = "Cannot divide by zero."
    match input_operator:
        case '+':
            result = f"The result is {num1 + num2}."
        case '-':
            result = f"The result is {num1 - num2}."
        case '*':
            result = f"The result is {num1 * num2}."
        case '/':
            result = f"The result is {num1 / num2}."
        case _:
            result = "Invalid operator."

print(result)
