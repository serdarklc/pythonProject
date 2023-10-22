
groceries_list = ['Egg', 'Milk', 'Rice']

groceries_list.append('Chicken')
groceries_list.extend(('Beef','Orange', 'Onion')) # We should use tuple,list,set

print(len(groceries_list))

"""groceries_list[-2:] = 'Cherry' # We should use tuple,list"""
groceries_list[-2] = 'Cherry'
print(groceries_list)

print("-------------------------------------------------")

numbers_list = [10,20,30,40,50,60,70,80]
print(numbers_list)

numbers_list[2:-2] = [300, 4000, 5, 60000]
print(numbers_list)

print("-------------------------------------------------")

characters = ['a','b','c','d','e','f','g','h','i']

list1 = characters[2:-3]
print(list1)

list2 = characters[:4]
print(list2)

list3 = characters[2:]
print(list3)

characters[2:5] = ['C','D','E','C','D','E','X','Y','Z']
print(characters)

print("-------------------------------------------------")

names = ['Conor', 'Steve', 'Hazel', 'Breana']

for x in names:
    print(x)

print("-------------------------------------------------")

nums = [10,20,30,40,50,60]

for i in range(0,len(nums)): # range(len(nums)) is same
    nums[i] = int(nums[i] / 5)
print(nums)

print("-------------------------------------------------")

nums = [10,20,30,40,50,60]

for i in reversed(range(len(nums))):
    print(nums[i])

print("-------------------------------------------------")

nums = [10,20,30,40,50,60]
for i in nums[::-1]:
    print(i)

print("-------------------------------------------------")

nums = [413,10000,120,330,640,50,60]

nums.sort()
print(nums)

"""ascending order"""
nums = [413,10000,120,330,640,50,60]
nums.sort(reverse=True)
print(nums)

print("-------------------------------------------------")

list1 = [10,20,30,40]

list1 = list(reversed(list1))
print(list1)

list1.reverse()
print(list1)

print("-------------------------------------------------")

tuple_elements = ('Java', 'Python', 'C#', 'Ruby')

list_elements = list(tuple_elements) # in order to convert from tuple to list
list_elements[-2] = 'C++'
list_elements.append('SWIFT')
print(list_elements)

tuple_elements = tuple(list_elements)
print(tuple_elements)

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

print(list1 is list2) # False because list is changeable, object is stored in memory separately

tuple1 = (1,2,3,4,5)
tuple2 = (1,2,3,4,5)

print(tuple1 is tuple2) # True because tuple is immutable

print("---------------------------------------------")

groceries_list = ['Egg', 'Milk', 'Rice']

groceries_list.append('Chicken') # single element will be added
groceries_list.extend(('Beef','Orange', 'Onion')) # multiple elements will be added
print(groceries_list)

groceries_list.remove('Beef')
print(groceries_list)

groceries_list.pop() # the last item will be removed automatically
print(groceries_list)

groceries_list.pop(1) # the item is placed on the first index will be removed
print(groceries_list)

groceries_list.insert(2,'Apple')
print(groceries_list)

print(groceries_list.index('Rice'))

groceries_list.append('Apple')
print(groceries_list.count('Apple'))

print('-----------Comprehensions--------------')

nums = []

for x in range(1,51):
    nums.append(x)

print(nums)
"""
new_list = []
for x in range(1,51):
    if x % 5 == 0:
        new_list.append(x)
print(new_list)
"""

new_list = [x for x in nums if x % 5 == 0]
print(new_list)

print("---------------------------------------------")
tuple3 = tuple ([x for x in nums if x % 5 == 0])  # tuple does not support comprehension
print(tuple3)

print("---------------------------------------------")

nums = []
for x in range(100):
    nums.append(x)
print(nums)

even_number = [x for x in nums if x % 2 == 0]
print(even_number)

odd_number = [x for x in nums if x % 2 != 0]
print(odd_number)

print("---------------------------------------------")

names = ['Python', 'Java', 'Java', 'JavaScript', 'java', 'JaVA', 'Ruby']

new_list = [x for x in names if x.upper() != 'JAVA']
print(new_list)






