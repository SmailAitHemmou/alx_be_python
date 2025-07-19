try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    input_operator = input("Choose the operation (+, -, *, /): ")

    match input_operator:
        case '+':
            print(f"The result is {num1 + num2}.")
        case '-':
            print(f"The result is {num1 - num2}.")
        case '*':
            print(f"The result is {num1 * num2}.")
        case '/':
            try: 
                print(f"The result is {num1 / num2}.")
            except ZeroDivisionError:
                print("Cannot divide by zero.")
        case _:
            print("Invalid operator.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
