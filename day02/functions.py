# method identification in Java
# public static void String(parameters){ }

"""which def is specified under the class is called METHOD
  otherwise is called function"""

import numbers

def display():
    print('Hello World')
    print('I love coding')

def value():
    return 10 #return method

print(value()*8)

def return_int() -> int:
    return 10.0

print(return_int())


def square(num1: int, num2: int) -> int : #arguments have to be int
    return num1 * num2

print(square(2,3))
print(square('string',9))
#print(square('string',10.6)) #we can see errors because of specified data type like int

def add(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2

print(add(10,20))
print(add(10.10, 45.78))

print('*******************************')

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

print(calculater(23, 45, '-'))


"""overloading"""

def sum(num1: numbers, num2: numbers, num3: int = 0, num4: int = 0):
    return num1 + num2 + num3 + num4

print(sum(10,20)) #num3 and 4 is accepted like 0
print(sum(10,20,30)) #num3 value is idendified from 0 to 30
print(sum(10,20,30,40)) # num4 value is changed from 0 to 40

class klas:
    def method(self): # this is a method not function
        pass

def concat(a: str, b= '', c= '', d= '', e= ''):
    print(f'{a},{b},{c},{d},{e}')

concat('BMW')
concat('BMW','Mercedes')
concat('BMW',4.20, 2024, 'M', '0 km')
concat('BMW','Mercedes','Tesla',False, True)
concat(23, 45, 56, 'string')

