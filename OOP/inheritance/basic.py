class person:
    def __init__(self,name):
        self.name=name

    def display(self):
        print(f"My name is : {self.name}")

class student(person):
    def __init__(self, name,rln):
        super().__init__(name)
        self.rln=rln

    def display(self):
        super().display()
        print(f"roll no : {self.rln}")


p1 = person("Ragu")
p2=person("nemi")
s1=student("ragu",23)
p1.display()
p2.display()
s1.display()
       