# types-->
# 1.single :one class inhinherit from >1 classes
# 2.multiple :one class inherit from more than one 
# 3.multilevel :sub class of another (super) class is a super class to another sub class
# 4.hybrid :more than one inheritance usage 

#2
class human:
    def work(self):
        print("i can work")
    
class male():
    def work(self):
        print("i can code ")
    
class boy(male,human):
    pass


b1=boy()
# human.work(b1)
# male.work(b1)
# b1.code()



#3 multilevel
# class grandfather:
#     def grandfather(self):
#         print("grandfather")
    
# class father(grandfather):
#     def father(self):
#         print("father")

# class son(father):
#     def person(self):
#         print("person")


# g=grandfather()
# p=son()
# p.grandfather()
# p.father()
# p.person()
