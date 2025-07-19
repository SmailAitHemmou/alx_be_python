# Step 1: Prompt the user to enter the pattern size
size = int(input("Enter the size of the pattern: "))

# Step 2: Initialize row counter
row = 0

# Step 3: Use a while loop for rows
while row < size:
    # Step 4: Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after finishing a row
    row += 1