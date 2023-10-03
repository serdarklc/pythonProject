#import functions

from utility import sum, calculater

result = sum(10,20)
print(result)

result = calculater(10, 20, '*')
print(result)

import utility
utility.sum(12,56)
utility.calculater()
utility.square(2,2)

"""Alias Name"""
import utility as u #in order to short form
u.square(3,5)
u.sum(10,20)

from utility import sum as s
print(s(10,20))
