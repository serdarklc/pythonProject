
if True :
    print('Python Programming')

if False:
    print('Python is not Programming')

print('Java Programming')

score = 70

if score >= 60:
    print(f'Congrats! your score {score} you passed the exam')

if score <= 60:
    pass    #temporary situation means will be identified later

s = 'Hello World'
if "H" and "W" in s:
    print(s, 'has', 'H and W')

age = 20
result = None

if age >= 21:
    result = 'Eligible'
else:
    result = 'Not eligible'
print(result)

#Ternary

age = 26
result = 'Eligible' if age >= 21 else 'Not eligible'

print(result)

print("---------------------------------------")

num = 100
result = None

if num > 0:
    result = "Positive"
elif num < 0:
    result = "Negative"
else:
    result = "Zero"

print(result)

print("---------------------------------------")

num = 200
#result2 = 'Positive' if num > 0 elif num < 0 'Negative' else 'Zero'  elif doesn't work in python as a ternary

print("---------------------------------------")

score = -300
#if score >= 0 and score <= 100:
if 0 <= score <= 100:
    if score >= 60:
        print('Passed')
    else:
        print('Failed')
else:
    print("invalid score")
