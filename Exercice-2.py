ch=input("Donner ch : ")
while not (ch[-1]=="."):
    ch=input("Donner ch : ")
k=" "
s=""
p=0
for i in range(len(ch)):
    if ch[i]!=k:
        s+=ch[i]
    else:
        if i+1<len(ch) and ch[i+1]!=k:
            s+=k
            p+=1
if s[-2]!=k:
    p+=1
print("mots: ",p)
print(s)