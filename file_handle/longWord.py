import os
with open("file_handle\words.txt","r") as file:
    words = file.read()

List = words.split()
long=""
# for w in List :
#     long = max(len(w),len(m))
#     m=w

for w in List:
    if len(w) > len(long):
        long=w
print("longest word : ",long)
print("longest word length: ",len(long))

          