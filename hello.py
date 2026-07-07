import numpy as np


def hello():
    return "Hello, world!"


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero!")
    return a / b


def sqrt(a):
    return np.sqrt(a)


def power(a, b):
    return np.power(a, b)


def log(a):
    return np.log(a)


def exp(a):
    return np.exp(a)


def sin(a):
    return float(np.sin(a).round(15))


def cos(a):
    return float(np.cos(a).round(16))


def tan(a):
    return float(np.tan(a).round(15))


def cot(a):
    if tan(a) == 0:
        return float("inf")
    return float((1 / np.tan(a)).round(16))


def __main__():
    hello()


if __name__ == "__main__":
    __main__()
