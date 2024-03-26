# Function to add two numbers
def add(x, y):
    return int(x + y)

# Function to subtract two numbers
def subtract(x, y):
    return int(x - y)

# Function to multiply two numbers
def multiply(x, y):
    return int(x * y)

# Function to divide two numbers
def divide(x, y):
    # Check if divisor is zero to avoid division by zero error
    if y == 0:
        return "Error! Division by zero."
    else:
        return int(x / y)

# Print Welcome Message
print()
print("\tWelcome To CodeWithHamza - Python Calculator")
print("\t------------------------------------")
print()

# Display menu for the user to select an operation
print("Select Operation:")
print("Enter 1. for Addition")
print("Enter 2. for Subtraction")
print("Enter 3.  for Multiplication")
print("Enter 4. for Division")
print()

# Loop to continuously prompt the user until a valid choice is made
while True:
    choice = input("Enter choice (1 / 2 / 3 / 4): ")

    # Check if the choice is one of the four valid options
    if choice in ('1', '2', '3', '4'):
        # Prompt the user to enter two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected operation based on the user's choice
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        break
    else:
        # Display error message for invalid input
        print("Invalid input")
