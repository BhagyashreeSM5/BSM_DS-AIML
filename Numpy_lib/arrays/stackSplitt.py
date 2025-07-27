# stacking :combining 2 / more arrays
# np.vstack() -> vertical stacking  or np.stack(),axis=0  
# np.hstack() -> horizontal stacking  or np.stack() ,axis=1
import numpy as np
a=np.array([1,2,3])
b=np.array([10,20,30])
print("a :",a ," \nb :",b)
print("vertical stack of a and b  :",np.vstack((a,b)))
print("horizontal stack of a and b  :",np.hstack((a,b)))
print("----------another method----------")
print("vertical stack of a and b  :",np.stack((a,b),axis=0))
print("horizontal stack of a and b  :",np.stack((a,b),axis=1))

print("default : ",np.stack((a,b)))


print("#--#"*8,"splitting ","#--#"*8)
c=np.array([ [1,2,3],[10,20,30] ])
print(c)
print("np.hsplit() coloumn splits : ",np.hsplit(c,3))
print("np.vsplit() coloumn splits : ",np.vsplit(c,2))


# copy()  ->copies data /array to another 
# view()  ->it also works like copying without creating new array by new memory 
# it is just hold same data any modify done hehre it affect original data