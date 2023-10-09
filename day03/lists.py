
groceries_list = ['Egg', 'Milk', 'Rice']

groceries_list.append('Chicken')
groceries_list.extend(('Beef','Orange', 'Onion')) # We should use tuple,list

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







