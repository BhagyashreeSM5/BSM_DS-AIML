class tooShortPass(Exception):
    def __init__(self):
        super.__init__("password is too short ")

class missingDigitException(Exception):
    def __init__(self):
        super.__init__("password should contain digits ")


psw =input("enter a password : ")
try:
    if len(psw) <= 5:
        raise tooShortPass()
    elif not any(char.isdigit() for  char in psw):
        raise missingDigitException()
    else:
        print("password : ",psw)
except tooShortPass as tsp:
    print("length error ",tsp)
except missingDigitException as de:
    print("digits error ",de)