import os
file = open("file_handle\inputpy.txt","r")
if os.path.exists("file_handle\inputpy.txt"):
    #print(file.read())
    print("file exist")
else:
    print("not exist!!! ")

print("reading a line " )
line=file.readline()
print(line)
l=file.read(6)
print("reading upto 6 :")
print(l)
file.close()

wf = open ("op1.txt","w")
wf.write("hello world ,it's file handling")
wf.close()

if os.path.exists("file_handle\op1.txt"):
    os.remove("file_handle\op1.txt")
    print("file deleteed ...")
else:
    print("not found !!")