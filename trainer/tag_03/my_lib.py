def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ArithmeticError("Division by zero attempted")
    return a / b

