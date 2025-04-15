# Simple Calculator in Python

def calculate():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")

    choice = input("Enter choice (1/2): ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1 * num2}")
    else:
        print("Invalid input")

# 🔐 Prevent this from running during import/test
if __name__ == "__main__":
    calculate()

