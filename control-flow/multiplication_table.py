  # Multiplication Table Generator :
number = int (input("Enter a number to see its multiplication table: "))
x = number
y = [1,2]
z = x * y
for z in range(1, 11):
    print(f"{x} x {z} = {x * z}")