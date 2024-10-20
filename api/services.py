# Name not clear. This one is for math operations.

def add(a:float, b: float) -> float:
    """
    return the sum of a and b
    """
    return a + b

def minus(a:float, b: float) -> float:
    """
    return the difference of a and b
    """
    return a - b

def multiply(a:float, b: float) -> float:
    """
    return the product of a and b
    """
    return a * b

def divide(a:float, b: float) -> float:
    """
    return the result of division of a and b
    """
    if b == 0:
        raise ValueError("The denomunator cannot be null")
    return a / b