  # Robust Division Calculator with Command Line Arguments :


def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Attempt division
        result = numerator / denominator
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
