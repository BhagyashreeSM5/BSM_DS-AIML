import os
# file = open("file_handle\inputpy.txt","r")
# lines=file.readlines()
# print(lines)
# print("no of line: ",len(lines))
# file.close()

with open("file_handle\inputpy.txt","r") as file :
    l=file.readlines()
print("no of line: ",len(l))
