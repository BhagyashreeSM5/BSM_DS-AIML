import pandas as pd

print(pd.read_csv("student.csv"))       #it loads data from a csv files into pandas datagframe 

# series  : it is 1D array (single coloumn of data)
# it holds string, numbers ,dates and other data type

print("-----------Series--------------")
data=pd.Series([10,20,30,40])
print(data)
data2=pd.Series([1,2,3,4],index=['a','b','c','d'])
print("with custom index : \n ",data2)
# we can also apply operations on series like adding a number series+1,s1+s2,
# accessing series element s[0] and s['a'] slicing 
# and basic math functions like max ,min,mean ,sum etc