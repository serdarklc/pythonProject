import numbers


def calculater(num1: numbers, num2: numbers, operator: str) -> numbers :
    if operator == '+' :
        return num1 + num2
    elif operator == "-":
        return  num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return 'Invalid transaction'

def square(num1: int, num2: int) -> int : #arguments have to be int
    return num1 * num2

def sum(num1: numbers, num2: numbers, num3: int = 0, num4: int = 0):
    return num1 + num2 + num3 + num4