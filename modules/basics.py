# modules are (.py)file that contain code which is reusable

# built-in -->like random ,Math and many more.
# user defined --> creted by users 
# external modules --> installed via pip (numpy,pandas)

# import module_name as short name
# from moduleName import fun_name  -->import specific function from module 

import my_module1 as mm     #-----------------------------------user-defined module
print("importing module ")
print(mm.sub(4,1))
# print(help("modules"))

from my_module1 import add
print("importing specific function ")
print(add(4,1))

from my_module1 import *
print("importing everything ")
print(mul(10,2))
print(div(10,2))


import random       #----------------------------------------built-in function
import math
print("printg random number 1-10 :",random.randint(1,10))
l=["apple","banana","mango","berries"]
print("random choice from list :",random.choice(l))
print("square root of 16 : ",math.sqrt(16))         #math.radians() ,math.factorial() , math.pi , math.cos()



import basic2
print("adding from importing  1 9: ",basic2.add(1,9))