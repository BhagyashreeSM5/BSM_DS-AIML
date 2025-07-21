# exceptiona are errors occur during excecution of programm 
# try-except block
a=10
b=int(input("enter a num: "))
try:
    c=a/b
    print(c)
except:
    print("error: cannpt divided by zero")
finally:
    print("finally block executes always")

    