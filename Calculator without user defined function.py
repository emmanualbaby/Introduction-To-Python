# Display the menu of operations
print("Simple Calculator")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user input for the operation
operation = input("Enter the number corresponding to the operation you want (1/2/3/4): ")

# Get user input for the numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the operation based on user choice
if operation == '1':
    result = num1 + num2
    print("The result of addition is:", result)
elif operation == '2':
    result = num1 - num2
    print("The result of subtraction is:", result)
elif operation == '3':
    result = num1 * num2
    print("The result of multiplication is:", result)
elif operation == '4':
    # Handle division by zero
    if num2 != 0:
        result = num1 / num2
        print("The result of division is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input. Please enter a number between 1 and 4.")