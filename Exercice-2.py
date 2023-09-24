ch=input("Donner ch : ")
while not (ch[-1]=="."):
    ch=input("Donner ch : ")
k=" "
s=""
for i in range(len(ch)):
    if ch[i]!=k:
        s+=ch[i]
    else:
        if i+1<len(ch) and ch[i+1]!=k:
            s+=k
print(s)