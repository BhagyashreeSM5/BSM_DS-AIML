import pandas as pd
import numpy as np

# df=pd.DataFrame({
#     'department':['cse','ise','physics','cse','math','ise','math'],
#     'score':[89,76,29,91,88,79,91],

# })
# print(df)
# group=df.groupby('department')
# print("grouping by department : \n",group)
# print("mean of score : \n",group['score'].mean())

# student = pd.DataFrame({
#     'id':[1,2,4],
#     'name':['alice','bob','charvi']
# })
# score=pd.DataFrame({
#     'id':[1,2,4],
#     'marks':[20,81,19]
# })
# print(student,"\n",score,"\n\n")
# merged=pd.merge(student,score)
# print("merged : \n ",merged)

df1=pd.DataFrame({
    'id':[1,2,4],
    'name':["guvi","charvi","plo"]
})

df2=pd.DataFrame({
    'id':[1,2,6],
    'marks':[10,20,40]
})
print(df1," \n ",df2 ,"\n")
print("join /merge operations \n")
# inner :intersects -->joins only matching keys
# outer :union --> all keys from both sides
# right :all from df2 ,match from left
# left :all from df1,macth from right
print("inner join : \n ")
print(pd.merge(df1,df2,on='id',how='inner'))
print("outer join : \n ")
print(pd.merge(df1,df2,on='id',how='outer'))
print("right join : \n ")
print(pd.merge(df1,df2,on='id',how='right'))
print("left join : \n ")
print(pd.merge(df1,df2,on='id',how='left'))

# concatenation of series and dataframes
# pd.concate(d1,df2,axis=0)
# axis=0 -->row conatenation
# axis=1 -->vertical concatenation


# map() -->used for element wise operations in series only ->series.map(func/dict)
# apply() -->both ->apply(func,axis=0/1),0->col ,1->row
s=pd.Series([1,2,4,6,7])
print("---"*24)
print(s,"\n using map() \n")
print(s.map(lambda x : x*10))
print(s.map(lambda y :y*y))

df=pd.DataFrame({
    'math':[10,20],
    'sci':[70,40]
})
print(df,"\n apply() \n ",df.apply(lambda x : x['math']+x['sci'],axis=1))

# applymap() ->apply only for dataframes
print("usimg applymap() : \n",df.applymap(lambda x : x*2))