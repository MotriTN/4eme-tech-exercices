#Exercice 4 serie 1
N=int(input(("Donner N : ")))
while not (5<=N<=150):
    N=int(input(("Donner N : ")))
s=1
for i in range (2,N+1):
    if i % 2 == 0:
        s -= 1 / i**2
    else:
        s += 1 / i**2
print(s)
