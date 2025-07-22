# polymorphism types-----
# method overriding 
# operator overiding
# method overloading
# duck typing

# ------duck typing----
# if an object has requireed methods & properties
# then it is treated as the type of that object


# class animal:
#     def talk(self):
#         print("spe")
    
# class dog(animal):
#     def talk(self):
#         print("bark")

# class cat(animal):
#     def talk(self):
#         print("meow")

# class car():
#     def talk(self):
#         print("drive")

# ani = [dog(),cat(),car()]  
# for a in ani:
#     a.talk()

    
    # it care only object has method or not 
    # it does't care  which class an object come from

class vehicle:
    def move(self):
        print("move")
    
class bike(vehicle):
    def move(self):
        print("two wheeler")

class car(vehicle):
     def move(self):
        print("four wheeler")
    
class bus():
    def move(self):
        print("8 wheeler")
    
def display(anything):
    anything.move()



display(car())
display(bike())
display(vehicle())
display(bus())