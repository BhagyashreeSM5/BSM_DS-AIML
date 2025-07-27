# to perform operstion of arrays of different size 
import numpy as np

a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([10,20,30])
c=np.array([10])
print("a -> ",a)
print("b -> ",b)
print("c -> ",c)

print("a+c : ",a+c)

print("a+b :",a+b)
# 1,2,3
# 4,5,6         #2*3

#10,20,30       #1*3

#there should be slight shape match then only it performs
# 10,20,30  --> 10,20,30
#               10,20,30

# 1,2,3     +   10,20,30      = 11 22 33        
# 4,5,6         10,20,30        14 25 36

