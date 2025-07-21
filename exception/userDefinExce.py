# user defined execeptions are created by using exception class
#      class exception_name(Exception )
#           pass
     

#writing msg in raise statement only
#1. class invalidException(Exception ):
#      pass

# mag in class,passess nothing
#2. class invalidException(Exception):
#     def __init__(self):
        #  super().__init__("age can't be exceeds 0-100 ") 


#3.raise statemnt passess msg ,here bby calling super method it displays
class invalidException(Exception):
     def __init__(self,msg):
          super().__init__(msg) 

age=int(input("enter a age : "))
if age < 1 or age > 100:
     raise invalidException("invalide age ,it should be 0-100 !!")
else:
     print("age : " ,age)
