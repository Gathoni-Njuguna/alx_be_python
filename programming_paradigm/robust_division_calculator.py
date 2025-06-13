def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return (f"The result of the division is {result}")
    except ZeroDivisionError:
        return (False, "Error: Cannot divide by zero.")
    except ValueError:
        return (False, "Error: Please enter numeric values only.")
