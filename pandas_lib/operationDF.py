
import pandas as pd
import numpy as np
data={
    'name':["alice","bob","maka"],
    'age':[20,29,27],
    'marks':[8,79,88]
}
df=pd.DataFrame(data)
print(df)

# df.at[row_name,col_name]=new_value
# df.loc[row_name,col_name]=new_value
df.at[1,'marks']=87
print("modifing marks of bob and age of alice: ")
df.loc[0,'age']=26
print(df)

print("------------------ADDING- NEW COLOUMN ----------------")
df['grade']=['A','S','O']
print("adding grade coloumn : \n",df)
df['passed']=df['marks']>= 80
print("\n ",df)
print("------------------ADDING NEW ROW ----------------")
df.loc[3]=['zoho',29,59,'C',False]
print(df)

print("------------------REMOVING ROWS/COLOUMN ----------------")
# df.drop(labels,axis,inplace=)
#label :index to remove
#axis :row 0 or coloumn 1
# inplace:True ->chnage original df and False -->no change
df2=df.drop('grade',axis=1,inplace=False)
print("after removing grade coloumn : \n",df2)
print("\n originsl data  \n",df)
df.drop(2,axis=0,inplace=True)
print("after removing 2nd row : \n",df)

print("------------------RENAMING ROWS/COLOUMN ----------------")
# inplace = flase it does't affect original one ,it is only upadate in new data
# df.rename(columns={old_name :new_name },inplace=)
print("renaming marks coloumn as score  : \n")
df.rename(columns={'marks':'score'},inplace=True)
print(df)
print("renaming index o as zero : ")
df.rename(index={'0':'zero'},inplace=True)
print(df)
print("-----------------SORTING  ----------------")
print(df.sort_values(by='score',ascending=False))

print("-----------------filling missing values ----------------")
df.loc[4]=["raani",np.nan,86,'A',True]
df.loc[5]=["guhi",27,np.nan,np.nan,False]
print(df)
print("checkining data is it null ? :\n ",df.isnull())
print("drop rows with null : \n ",df.dropna())
print("filling the missing value with 0 : ",df.fillna(0))



