name = input()
print(name)

# print(help(input)) in order to see details about method we can use help method
"""input always returns str"""
name = input('What is your name\n')
age = int(input('What is your age\n'))
gpa = float(input('What is your gpa\n'))
boolean_value = bool(input('Enter True or False'))

print(type(name))
print(type(gpa))
print(name, age, gpa)
