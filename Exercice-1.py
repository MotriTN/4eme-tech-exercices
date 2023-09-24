#Exercice 4 serie 1
N=int(input(("Donner N : ")))
while not (5<=N<=150):
    N=int(input(("Donner N : ")))
s=1
i=2
while i<=N:
    s-=1/N**2
    i+=2
i=3
while i<=N:
    s+=1/N**2
    i+=2
print(s)
