import numpy as np

arr1=np.array([1,2,3,4,5,6,7])
arr2=np.array([[1,2,3],[4,5,6]])
print("accessing-----------------------")
print(arr1)
print(arr2)
print("arr1[0] :",arr1[0])
print("arr1[-1] : ",arr1[-1])

print("arr2[1:2] : ",arr2[1:2])
print("arr2[1:-1] : ",arr2[1:-1])

print("Slicing-----------------------")
print("arr1[1:4] : ",arr1[1:4])
print("arr1[:] : ",arr1[:])
print("arr1[:5] : ",arr1[:5])
print("arr1[3:] : ",arr1[3:])
print("arr1[::2] : ",arr1[::2])
print("arr1[::-1] : ",arr1[::-1]) #reversing



#array operations 
# note : arrays size should be same here 

print("array operations--------------------------------")
a=np.array([1,2,3,4])
b=np.array([5,6,7])
print(a)
print(b)
print("a+b : ",a+b)
print("a-b :",a-b)
print("a/b : ",a/b)
print("a*b :",a*b)
print("a**2 : ",a**2)
