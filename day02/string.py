name = "Python"

print(len(name))
print(name[0])
print(name[len(name) -1]) #in order to find last character
print(name[-1])

s = 'Java Programming Language'
s2 = s[5:16]
print(s2)

s3 = s[:3]
print(s3)

s4 = s[:-1]
print(s4)

s5 = s[::-1]
"""reversing"""
print(s5) #for getting reversed format

print(s)
s6 = str(reversed(s)) # type was reversed before casting
print(s6)
s6 = reversed(s6)
print(s6)

s = s.capitalize() #just first character is made it capital
print(s)

s = s.title() #first of characters are capitalized
print(s)

s = "                 Python          "
s = s.strip() #trim method of Java
#rstrip => right trim
#lstrip => left trim
print(s)

s = 'JAVA'
print(s.index('A'))
print(s.rindex('A'))

s = 'JAVA JAVA'
s = s.replace('JAVA', 'Python')
print(s)

s = 'java java java'
s = s.replace('java', 'Python',2)
print(s)

s = 'java java java'
s = s.replace(' java', ' C++')
print(s)

s = 'java JAVA jAVA JaVA C++ C# C#'
print(s.count('java'))
print(s.lower().count('java'))

s1 = 'java'
s2 = 'JAVA'
print(s1.lower() == s2.lower())
