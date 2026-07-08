# 1.2 python - "hello" 

import numpy as np


def hello():
    return "Hello, world!"


def add(a, b):
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        return a + b
    raise TypeError("Both arguments must be integers or floats.")


def sub(a, b):
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        return a - b
    raise TypeError("Both arguments must be integers or floats.")


def mul(a, b):
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        return a * b
    raise TypeError("Both arguments must be integers or floats.")


def div(a, b):
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        if b == 0:
            raise ValueError("Can't divide by zero!")
        return a / b
    raise TypeError("Both arguments must be integers or floats.")


def sqrt(a):
    if (isinstance(a, int) or isinstance(a, float)):
        if a < 0:
            raise ValueError("Can't square root a negative number!")
        return np.sqrt(a)
    raise TypeError("Argument must be an integer or float.")


def power(a, b):
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        if b < 0:
            return 1 / np.power(a, -b)
        return np.power(a, b)
    raise TypeError("Both arguments must be integers or floats.")


def log(a):
    if (isinstance(a, int) or isinstance(a, float)):
        return np.log(a)
    raise TypeError("Argument must be an integer or float.")


def exp(a):
    if (isinstance(a, int) or isinstance(a, float)):
        return np.exp(a)
    raise TypeError("Argument must be an integer or float.")


def sin(a):
    if (isinstance(a, int) or isinstance(a, float)):
        return np.sin(a)
    raise TypeError("Argument must be an integer or float.")


def cos(a):
    if (isinstance(a, int) or isinstance(a, float)):
        return np.cos(a)
    raise TypeError("Argument must be an integer or float.")


def tan(a):
    if (isinstance(a, int) or isinstance(a, float)):
        return np.tan(a)
    raise TypeError("Argument must be an integer or float.")


def cot(a):
    if (isinstance(a, int) or isinstance(a, float)):
        if a % (2*np.pi) == 0:
            return float("inf")
        elif a % np.pi == 0:
            return float("-inf")
        return 1 / np.tan(a)
    raise TypeError("Argument must be an integer or float.")


def __main__():
    hello()


if __name__ == "__main__":
    __main__()
