# Simple Calculator Program
# Function to perform addition
def add(x, y):
    return x + y
# Function to perform subtraction
def subtract(x, y):
    return x - y
# Function to perform multiplication
def multiply(x, y):
    return x * y
# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
# Main function to drive the calculator
def calculator():
    # Prompt the user to input two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return  
    # Display operation choices
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Prompt the user to choose an operation
    choice = input("Enter the operation number (1/2/3/4): ")

    # Perform the calculation based on user choice
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        print("Invalid operation choice!")
        return
    
    # Display the result
    print(f"The result is: {result}")

# Run the calculator
calculator()
