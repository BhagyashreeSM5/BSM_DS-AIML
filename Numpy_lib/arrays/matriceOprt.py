import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a,end="\n-------\n")
print(b)
print("dot product \n",np.dot(a,b) )

print("----------comparison operations ----------")
arr=np.array([1,24,67,98,231,12])
print("arr > 22 : ",arr>22)
print("arr==20  : ",arr==20)
print("arr != 10 : ",arr != 10)
print("comparison to extract specific part : ")
print(" arr[arr > 22] : ",arr[arr > 22])
print("arr[arr == 20] : ",arr[arr == 20])
print("arr[arr !=10 ] : ",arr[arr!=10])
print("\n -----------logical operations---------")
a=np.array([10,20,30,40,50])
mask=np.logical_and(a>12 ,a<48)
a=np.array([10,20,30,40,50])
print("\n",a)
print("logical and a>12 and a<40 : ",a[mask])
print("using or a==10 | a==40 : ",a[(a==10) | (a==40)])


#np.any() -->returns true if any condition is true 
#np.all() --> returns true if all conditions are true
print("np.any(arr > 40) : ",np.any(a > 40))
print("np.all(arr > 40) : ",np.all(a > 40))
print("np.all(arr > 8) : ",np.all(a > 8))
