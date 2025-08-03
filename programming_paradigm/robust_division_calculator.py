# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division and handle errors:
    - Non-numeric inputs
    - Division by zero
    Returns a formatted string with result or error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."