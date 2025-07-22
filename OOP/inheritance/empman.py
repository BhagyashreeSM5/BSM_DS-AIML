class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(f"name : {self.name}\nsalary:{self.salary}")

class manager(employee):
    def __init__(self,name,salary,dep):
        super().__init__(name,salary)
        self.dep=dep

    def display(self):
        print("---------manager-----------")
        super().display()
        print("department : ",self.dep)


print("---------employees-----------")
e1=employee("dennie",2324)
e2=employee("richard",7565)
m1=manager("bibuy",29373,"sde")
m2=manager("claury",4655,"cyber")

e1.display()
e2.display()
m1.display()
m2.display()
