  # Simple Calculator with Match Case :
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
input_operator = input("Choose the operation (+, -, *, /): ")
match input_operator:
    case '+':
        print(f"The result is {num1 + num2}.")
    case '-':
        print(f"The result is {num1 - num2}.")
    case '*':
        print(f"The result is {num1 * num2}.")
    case '/': 
        print(f"The result is {num1 / num2}.")