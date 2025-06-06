def perform_operation():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2
        else:
            return "Error: Invalid operation. Choose 'add', 'subtract', 'multiply', or 'divide'."
    except ValueError:
        return "Error: Invalid number input. Please enter a valid number."

# Example usage
result = perform_operation()
print("Result:", result)
