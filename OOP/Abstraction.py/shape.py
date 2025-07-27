from abc import ABC ,abstractmethod
class shapes(ABC):
   
    @abstractmethod
    def area(self):
        pass


class circle(shapes):
    def __init__(self,r):
        self.r=r

    def area(self):
        return 3.14*self.r*self.r
    
class rectangle(shapes):
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b
    

c=circle(2)
r=rectangle(2,8)
print("araea of circle : ",c.area())
print("araea of rectangle : ",r.area())