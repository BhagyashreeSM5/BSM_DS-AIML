# dataframe is like combination of rows and coloumn with label

import pandas as pd
data={
    'name':["alice","bob","maka"],
    'age':[20,29,27],
    'marks':[98,79,88]
}
df=pd.DataFrame(data)
print(df)
# acessing 
print("acessing coloumn : ",df['name'])
print("acessing multiple coloumn : ",df[['marks','age']])
print("acessing cell values : ",df.loc[0])  # by label/index
print("accessing cell values : ",df.iloc[1])        # by position
print("acessing cell values : ",df.loc[1,'name'])
print("accessing cell values : ",df.iloc[2,2])
print("filter row by condition age>20 :\n ",df[df['age']>20])