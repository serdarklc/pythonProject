class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'

class Employee(Person):

    def __init__(self, name : str, age: int, job_title: str, company_name: str = 'Unknown', salary: int = 0):
        '''after first giving default value for argument , then rest of argument needs to default value'''
        super().__init__(name, age)
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')
class Developer(Employee):
    def __init__(self, name: str, age: int, job_title: str = 'Software Developer'):
        super().__init__(name, age, job_title)

    def work(self):
        print(f'{self.job_title} {self.name} is coding')

class Teacher(Employee):
    def work(self):
        print(f'{self.name} is teaching')

employee1 = Employee('Serdar', 35, 'QA Engineer')
developer1 = Developer('Hakan', 42)
teacher1 = Teacher('Deniz', 30, 'English Teacher')

print(employee1)
print(developer1)
print(teacher1)

employee1.work()
developer1.work()
teacher1.work()
