def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input types"

# Example of using the function with an uncommon error
print(function_with_uncommon_error(10, 0))
print(function_with_uncommon_error(10, "hello"))
print(function_with_uncommon_error(10, 2))