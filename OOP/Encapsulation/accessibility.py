class parent1:
    def __init__(self):
        self.pub=10
        self._pro=20
        self.__pri=30

    def show(self):
        print(f"--------in parent \npublic : {self.pub}\nprotected : {self._pro}\nprivate :{self.__pri}")

class child1(parent1):
    def display(self):
        print(f"---------in child \npublic : {self.pub}")
        print(f"protected : {self._pro}")
        # print(f"private :{self.__pri}") #shows error and we can use setter getter method

    
p=parent1()
p.show()
c=child1()
c.display()