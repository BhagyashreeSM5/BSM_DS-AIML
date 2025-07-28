# these are also numpy arrays allows to hide/ignore
# uses :
# to handle missing/bad data 
# to perform opearations ignoring those values

# creation
import numpy.ma as ma
data1=ma.array([10,20,-1,-2,0,200],mask=[0,0,1,0,1,1])
data2=ma.array([1,2,3,4,9,6],mask=[True,True,False,True,False,False])
print("masked array using 0 & 1's : ",data1)
print("masked array using true and false2 : ",data2)
print("using conditions to mask ------------------------")
data3=ma.masked_less([1,-3,-2,26,19,0,-9],0)
print("data3 : ",data3)

print("array mean : ",data3.mean())
print("masked elements in data3 : ",data3.mask)
data4=ma.masked_equal(data3,-3)
print("data4 : ",data4)