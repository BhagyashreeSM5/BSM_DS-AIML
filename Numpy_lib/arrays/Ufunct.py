# Ufunct  : universal functions
# they are afst,element-wise functions provided by numpy 
# perform operations on array without wrtoing loops

import numpy as np

arr=np.array([1,2,3,4])
print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))
print(np.sin(arr))
print(np.abs(arr-10))


print("------aggregation function------------")
#used to summarise the data -essential in ml for calculating loss,mean,variance
print("sum : ",np.sum(arr))
print("mean : ",np.mean(arr))
print("min element : ",np.min(arr))
print("max element : ",np.max(arr))
print("std variance : ",np.std(arr))
print("variance : ",np.var(arr))

print("---------- basic function ------------------")
a=np.array([1,2,3,4,5])
print("sum : ",np.sum(a))
print("product : ",np.prod(a))
print("cumulative sum : ",np.cumsum(a))
print("difference b/t consecutive nums  : ",np.diff(a))
print("---------- statistical function ------------------")
print("mean : ",np.mean(a))
print("median : ",np.median(a))
print("std deviation : ",np.std(a))
print("std variance : ",np.var(a))
print("max and min : ",np.max(a),np.min(a))
print("index of max and min : ",np.argmax(a),np.argmin(a))
print("---------- aggregation function ------------------")
print("np.sum(a,axis=0) : ",np.sum(a,axis=0))           #   coloumn sum
print("np.sum(a,axis=1) : ",np.sum(a,axis=1))           #   rows sum
print("---------- rounding function ------------------")
b=np.array([2.16,4.98,9.76])
print(b)
print("np.round(b) : ",np.round(b))
print("np.floor(b) : ",np.floor(b))
print("np.ceil(b) : ",np.ceil(b))

