def perform_operation(num1, num2, operation):
    """
    Performs arithmetic operations on two numbers.
    
    Args:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide').
    
    Returns:
        float | str: Result of the operation or an error message.
    """
    operation = operation.lower().strip()  # Normalize input
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Choose 'add', 'subtract', 'multiply', or 'divide'."
