from math import *
ch=input("Donner le nombre complexe: ")
p=ch.find("+")
a=ch[:p]
b=ch[p+1:len(ch)-1]
while not (a.isdecimal()==True and b.isdecimal()==True and p!=-1 and ch.find("i")!=-1):
    ch=input("Donner le nombre complexe: ")
    p=ch.find("+")
    a=ch[:p]
    b=ch[p+1:len(ch)-1]
print(sqrt(int(a)**2+int(b)**2))
