  # Simple Calculator with Match Case :
num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))
operation = input("choose the operation (+, -, *, /): ")

match operation:
    case '+':
        result = num1 + num2
        print("The result is:", result)
    case '-':
        result = num1 - num2
        print("The result is:", result)
    case '*':
        result = num1 * num2
        print("The result is:", result)
    case '/':
        if num2 == 0:
            print("cannot divide by zero")
        else:
            result = num1 / num2
            print("The result is:", result)
    case _:
        print("Invalid operation")