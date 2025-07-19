# Multiplication Table Generator
number = int(input("Enter a number to see its multiplication table: "))
X = number 
print(f"Multiplication table for {number}:")
for Y in range(1, 11):
    Z = X * Y
    print(f"{X} * {Y} = {Z}")