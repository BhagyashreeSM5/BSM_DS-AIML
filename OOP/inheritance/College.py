class person:
    def __init__(self,name,gen):
        self.name=name
        self.gen=gen

    def display(self):
        print(f"Name: {self.name} \nGender: {self.gen}")


class proffesor(person):
    def __init__(self,name,gen,dep,salary):
        super().__init__(name,gen)
        self.dep=dep
        self.salary=salary
    
    def display(self):
       super().display()
       print(f"Deparment: {self.dep} \nSalary: {self.salary}")

class student(person):
    def __init__(self, name, gen,rln,branch):
        super().__init__(name, gen)
        self.rln=rln
        self.branch=branch

    def display(self):
        super().display()
        print(f"Roll no: {self.rln} \nbranch: {self.branch}")
    

class researchAssi(proffesor,student):
    def __init__(self,name,gen,dep,salary,rln,branch,project_name):
        
        proffesor.__init__(self,name,gen,dep,salary)
        student.__init__(self,name,gen,rln,branch)
        self.project_name=project_name

    def display(self):
        super().display()
        print(f"Project name:{self.project_name}")

    
# r=researchAssi("akashi","f","cse",30000,20,"cse","wind mil")
# r.display()

s=student("akashi","f",20,"cse")
s.display()
p=person("anand","m")
p.display()
pr=proffesor("bhavana","f","cse",300000)
pr.display()