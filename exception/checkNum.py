class NotEvenException(Exception ):
    def __init__(self,a):
        print("number is not even ",a)


class NotNumberException(Exception):
    def __init(self,msg,a):
        super.__init__(msg)
        print(a)



a=int(input("enter a number : "))

try:
    if a%2 != 0:
        raise NotEvenException(a)
    else:
        print("even number: ",a)
except :
    raise NotNumberException("not a number",a)

