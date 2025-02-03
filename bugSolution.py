def function_with_improved_error_handling(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return f"Error: {e}"

# Example of using the improved function
print(function_with_improved_error_handling(10, 0))
print(function_with_improved_error_handling(10, "hello"))
print(function_with_improved_error_handling(10, 2))
print(function_with_improved_error_handling("10",2))