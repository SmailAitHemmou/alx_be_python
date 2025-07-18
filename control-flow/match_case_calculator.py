  # Simple Calculator with Match Case :
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
input_operator = input("Choose the operation (+, -, *, /): ")
match input_operator:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        result = num1 / num2
        print(f"The result is {result}.")