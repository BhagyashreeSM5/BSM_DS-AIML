vowels=0
vset ="aeiouAEIOU"
consonents=0
digits=0
file=open("file_handle\inp2.txt","r")
content = file.read()
for char in content:
    if char.isalpha():
        if char in vset:
            vowels=vowels+1
        else:
            consonents=consonents+1
    else:
        digits = digits+1

print(f"vowels : {vowels} \n consonents : {consonents} \n digits : {digits}")
