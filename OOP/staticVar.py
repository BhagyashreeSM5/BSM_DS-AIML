class staticVarCls:

    @staticmethod
    def factorial(n):
        f=1
        for a in range(1,n+1):
            f*=a
        return f

    @staticmethod
    def convert(t):
        return 9/5 * t + 32 
    


print("factorial of a number : ",staticVarCls.factorial(5))
print("convert celcius to farhenhit : ",staticVarCls.convert(2))
