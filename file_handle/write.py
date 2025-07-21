import os
msg=input("enter a message : ")
fw = open("op2.txt","w")
fw.write(msg)
fw.close()
