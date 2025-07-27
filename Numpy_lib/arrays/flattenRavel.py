# flatten() -->turns multi-dimentional array into 1D array,it returns copy
import numpy as np
arr2 = np.array([[1,2,5],[3,4,6]])
flat=arr2.flatten()
print("flatten array of :",arr2 ,"to ",flat)

# resize() -->resize the array (it adds 0 if needed),
# it changes existing arraya(not return new one)

a=np.array([1,2,3,4,5,6])
print(a)
resha=a.reshape(2,3)   # new size should match no of elements 
print("reshaped of a :",resha)
resArr=a.resize(2,3)
print(f"resized array of {a} ")     # no needed to match

#Ravl() -->similar to flatten but returns view not a copy
rav=arr2.ravel()
print(f"ravel of  {arr2} : {rav}")

print("---------------seeing difference flatten and ravel ----------------")

b=np.array([[10,20],[30,40]])
print("original array : ",b)

flatAr=b.flatten()
print("flatten array : ",flatAr)

rvl=b.ravel()
print("ravel array : ",rvl)

flatAr[0]=100
rvl[1]=200
print("after changing flat[0]=100 rvl[1]=200 : ")
print("original array : ",b)
print("flatten array : ",flatAr)
print("ravel array : ",rvl)

#any changes done for ravel will affect original array ,,
# but changes on flatten does't affect original array
