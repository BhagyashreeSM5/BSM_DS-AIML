# # abstraction :hiding complex implementation showing only essential features
# syntax :

# from abc import ABC,abstractmethod
# class clName(ABC)
#     @abstractmethod
#     def 
#       pass

# abc --> abstract base class 
# we cannot create object of abstract class

from abc import ABC,abstractmethod

class animal(ABC):  
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print("bark")

 
# a=animal()
# a.sound()
d=dog()
d.sound()