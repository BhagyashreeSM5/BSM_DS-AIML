# else blocks executes only whe  no error ocuurs 
# both finally and executes looks to work  for same
# finally is also used to clean up code ,release resources and it always executs
# with irrespective of excetion occur(not occur)
# but else executes only no error exception occurs 

a=4
b=int(input("enter a num "))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("error:zero Division Error")
except ValueError:
     print("error:value Error")
    
else:
    print("exception not occur ")

