import pandas as pd
import numpy as np

records=[]
while True:
    date=input("enter a date (yyyy-mm-dd) : ")
    category=input("enetr a category :")
    amt=input("enter amount :")
    payment_mode=input("enter  payment mode :")
    records.append([date,category,amt,payment_mode])
    count=input("do you want add another (yes/no)?? ").lower()
    if count != 'yes':
        break

df=pd.DataFrame(records,columns=['date','category','amount','payment_mode'])

print(df)
df['date']=pd.to_datetime(df['date'])
df['day']=df['date'].dt.day_name()
print("--------------------- \n",df)
df['amount']=df['amount'].astype(float)
total=df['amount'].sum()
print("--"*20,"\n Total expenses : ",total,"\n","--"*20)
