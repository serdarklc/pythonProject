
class Person:
    def __init__(self, name: str, age: int):
        self.__name = None # private
        self.__age = None # private
        self.set_name(name)
        self.set_age(age)

    # self is used for declaring and accessing

    '''getter'''
    def get_name(self) -> str:
        if self.__name is None or self.__name == '' or type(self.__name) != str: # we can add conditions for getter
            raise RuntimeError(f'Invalid name has been set: {self.__name}') # raise like exception in Java

        return self.__name # for getter method we can return

    """setter"""
    def set_name(self, name: str):
        if type(name) != str:
            raise RuntimeError('Person name must be string')

        if name == '':
            raise RuntimeError('Person name cannot be empty')

        self.__name = name

    """ -> makes def's return int"""
    def get_age(self) -> int:
        return self.__age

    def set_age(self, age) -> int:
        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid age {age}')
        self.__age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'  # concatenation


person1 = Person("Dibagio", 47)
#person1 = Person(1234)
#person1.set_name('Serdar')
print(person1.get_name())
print(person1.get_age())
