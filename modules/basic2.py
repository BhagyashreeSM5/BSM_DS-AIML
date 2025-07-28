# __name__  :built-in variable in python ,python
#  sets this value automatically for every module 
# __main__ :a normal string ,when we run file directly 
#  python sets __name__ == __main__ for that file


# this hepls to test /demo the code
# consider this file as an module
# it only runs when you run this module directly doe't run when we import to another file 
def add(a,b):
    return a+b


if __name__ == "__main__":
    print("testing----")
    print(add(4,9))
