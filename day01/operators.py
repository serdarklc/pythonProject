# arithmetic +,-,*,/

print(10 -2)
print(10*8)

"""division returns always float result"""
print(10/3)
print(10/5)

print(10%3)

"""logical operators"""
s = "Hello World"
print("H" and "W" in s) #True

print(True and True)
print(True or False)

s = "Java Python C# C++"
print("Java" or "Ruby" in s) #Java
print("Java" in s or "Ruby" in s) #True

age = 29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'
print(is_eligible)

has_java = 'Java' in s
print(has_java)

""" !contains()"""
print('Python' not in s)

print(not False) #not operation is used with boolean
print(not True)

s = 'Java'
s2 = 'Java'

print(s is s2) # True # referencing the same objects (== operators of java)



