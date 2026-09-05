def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
    
def power(base, exponent):
    return base ** exponent

def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b

def cube(n):
    return n ** 3

def percentage(part, whole):
    return (part / whole) * 100
