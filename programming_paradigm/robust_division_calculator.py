def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
        print(result)
    except ZeroDivisionError:
    # Code to run if a ZeroDivisionError occurs
        print("Cannot divide by zero!")
    except ValueError:
    # Code to run if a ValueError occurs
        print("Invalid input")
    except:
    # Code to run if any other error occurs
        print("An unexpected error occurred")
    finally:
    # Code to run regardless of whether an exception occurred
        print("This will always execute")
