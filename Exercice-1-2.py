N=int(input(("Donner N : ")))
while not (5<=N<=150):
    N=int(input(("Donner N : ")))
s=1
i=0
for i in range (2,N+1,2):
    s-=1/N**2
for i in range (3,N+1,2):
    s+=1/N**2
print(s)