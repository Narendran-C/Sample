def calculate(num1, operator, num2):
    if not isinstance(num1, (int, float) or not isinstance(num2, (int, float))):
        raise ValueError("Both parameters should be integers.")

    if operator not in ('+', '-', '*', '/'):
        raise ValueError("Invalid operator, use '+', '-', '*', or '/'.")

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2


result = calculate(10.2252, '+', 5.2536)
print(f"Result: {round(result, 5)}")
