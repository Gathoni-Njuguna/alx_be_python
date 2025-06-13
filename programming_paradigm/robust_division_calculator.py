def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return (True, result)
    except ZeroDivisionError:
        return (False, "Error: Cannot divide by zero!")
    except ValueError:
        return (False, "Error: Both inputs must be numeric!")
