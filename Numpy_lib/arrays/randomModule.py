#  used to pick random numbers/elements

# np.random.rand()  --> random float number
# np.random.randn()   -->random float from normal distribution
# np.random.randint() -->random int from start,end,step
# np.random.choice()  -->from list /array
# np.random.seed()    -->set seed for reproducible results


import numpy as np

print("np.random.rand(3) : ",np.random.rand(3))
print("np.random.randint(1,10,2) : ",np.random.randint(1,10,2))
print("np.random.choice([1,4,9,10,2]) : ",np.random.choice([1,4,9,10,2]))
print("np.random.choice([1,4,9,10,2],size=4) : ",np.random.choice([1,4,9,10,2],size=4))
print("np.random.randn(3) : ",np.random.randn(3))
np.random.seed(42)      #this only fix randomeness for reproducibility ,
                        #it sets the starting point of random number generator

print(np.random.rand(3))        #actually it generates the number 

