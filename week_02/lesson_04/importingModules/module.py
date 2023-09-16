#Math in Javascript is an example of a module 

my_name = 'Ayana'

#This module is being used in userInput.py and test.py. it does not work in userInput.py because you cannot use modules in the same level as you but not the same folder. must be same folder or higher directory 

import math
import random


#

factorial = math.factorial(5)
print(factorial)

#random number 

random_number = random.randrange(0, 100)
print(random_number)