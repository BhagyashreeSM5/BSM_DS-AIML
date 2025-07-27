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