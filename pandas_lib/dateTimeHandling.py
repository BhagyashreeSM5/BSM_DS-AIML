# date 30-7-2025 is just a string but pandas help us to convert datatime object
import pandas as pd
import datetime
# date=datetime.now()
# print(date)
date_obj=pd.to_datetime(['2025-07-02','2025-01-26','2025-9-15'])
print(date_obj)

df=pd.DataFrame({
    'name':['neuor','sacro','shree','bob','ploui'],
    'join_date':pd.to_datetime(['2023-07-26','2021-08-10','2027-07-26','2005-01-26','2015-9-15'])
})
print("---------\n",df)
df['day']=df['join_date'].dt.day_name()
print("---------\n",df,"\n \n filtering-------------------")
print(df[df['join_date'] > '2022-01-01'])
# print(df[df['join_date'] > datetime.datetime(2015,1,1)])
today=pd.to_datetime('today')
df['Working days']=(today-df['join_date']).dt.days
print("\n \n",df)