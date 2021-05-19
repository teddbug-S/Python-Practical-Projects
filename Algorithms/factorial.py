

def factorial(x: int) -> int:
    """ Returns the factorial of 'x' """
    result = x
    while x != 1:
        result *= (x:=-1)
    return result
