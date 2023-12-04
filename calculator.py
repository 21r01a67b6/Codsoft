def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number:"))

            print("\nOperations:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
    

            operation = input("Choose an operation (1/2/3/4): ")

            if operation in ('1', '2', '3', '4'):
                if operation == '1':
                    result = add(num1, num2)
                elif operation == '2':
                    result = subtract(num1, num2)
                elif operation == '3':
                    result = multiply(num1, num2)
                elif operation == '4':
                    result = divide(num1, num2)

                print(f"Result: {result}")
            else:
                print("Invalid operation. Please choose a valid operation.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()