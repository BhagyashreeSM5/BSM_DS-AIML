# raise keyword used to trigger exception manually
age=int(input("enter a age : "))
if( age < 1 or age>100):
    raise ValueError("error: age should be in 1-100 ")

print("age: ",age)