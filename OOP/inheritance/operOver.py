# operator overriding :change the meaning of operator
# + can use to add and concate 
# here are special methods ( double underscore methods) to achieve this
# __add__ , __sub__ and etc


# print(1+1)
# print('1'+'1')

# class complexno:
#     def __init__(self ,r,i):
#         self.r=r
#         self.i=i
    
#     def __add__(self,other):
#         real=self.r + other.r 
#         image=self.i + other.i
#         print(f"{self.r}+{self.i}i")
#         print(f"{other.r}+{other.i}i")
       
#         print(f"ans : {real}+{image}i")
    
# c = complexno(3,1)
# b = complexno(1,1)
# c+b

class student:
    def __init__(self,marks):
        self.marks=marks

    def __ge__(self,other):
        if self.marks > other.marks:
            return True
        else:
            return False

s1=student(18)
s2=student(67)

if s1 >= s2 :
    print("student one got heighest ")
else:
    print("student two got heighest ")
