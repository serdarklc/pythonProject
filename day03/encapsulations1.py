
class Person:
    def __init__(self):
        self.__name = None # private
        self.__age = None # private

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

person1 = Person()
person1.set_name('Serdar')
print(person1.get_name())
