  # Simple Calculator with Match Case :
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
input_operator = input("Choose the operation (+, -, *, /): ")
match input_operator:
    case '+':
        result = int(num1) + int(num2)
        print(f"The result is {result}.")
    case '-':
        result = int(num1) - int(num2)
        print(f"The result is {result}.")
    case '*':
        result = int(num1) * int(num2)
        print(f"The result is {result}.")
    case '/':
        try:
            result = int(num1) / int(num2)  # will raise ZeroDivisionError if num2 == 0
            print(f"The result is {result}.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")