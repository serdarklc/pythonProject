class Person:

    def __init__(self, name, age):
        self.__name = None
        self.__age = None
        self.person_name = name
        self.person_age = age
        
    @property
    def person_name(self):
        if self.__name is None or self.__name == '' or type(self.__name) != str: # we can add conditions for getter
            raise RuntimeError(f'Invalid name has been set: {self.__name}') # raise like exception in Java
        return self.__name
    
    @person_name.setter
    def person_name(self, name):
        if type(name) != str:
            raise RuntimeError('Person name must be string')

        if name == '':
            raise RuntimeError('Person name cannot be empty')

        self.__name = name

    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, age):
        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid age {age}')
        self.__age = age


person = Person("Serdar", 100)
print(person.person_name)
print(person.person_age)
