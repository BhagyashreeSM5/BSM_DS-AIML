file=open("file_handle\inp2.txt","r")
opf = open("reverfile","w")
for line in file:
    rl=line[::-1]
    opf.write(rl+"\n")

file.close()
opf.close()


