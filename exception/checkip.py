a=input("enter " )
try:
    if a.isalpha():
        print("alphabet")
    elif a.isdigit():
        if int(a)%2 == 0:
            print("even")
        else:
            print("odd")

    else:
        raise ValueError("invalide error enter valide values ")
except Exception as e:
    print(e)
    