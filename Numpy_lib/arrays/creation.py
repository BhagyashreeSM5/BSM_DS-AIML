import numpy as np

#creating arrays
arr1=np.array([1,2,3])
print("1d array : ",arr1)
arr2 = np.array( [ [1,2,1],[3,4,3] ])
print("2d arrya : \n ",arr2)

# create range of numbers
#1)np.arange (start ,stop,step) :creates a number b/t start and stop
#2)np.linspace(start,stop,num) :creates evenly separated values  b/w start stop (inclusively)

arr3 = np.arange(1,10,2)
print("array by np.arange : ",arr3)

arr4=np.linspace(1,2,5)
print("array by np.linspace : ",arr4)


#--Properties---
print("-"*25+"properties")
print("no of dimension arr2.ndim : ",arr2.ndim)
print("no of rows & coloums arr2.shape : ",arr2.shape)
print("no of elements arr2.size : ",arr2.size)
print("type of elements arr2.dtype : ",arr2.dtype)
carr=arr1.copy()
print("coping array to another copy() : ",carr)
print("transpose of array arr1.T : ",arr1.T)
print("transpose of array arr2.T : ",arr2.T)
print("rearranging elements arr2.reshape(new shape ) : ",arr2.reshape(3,2))