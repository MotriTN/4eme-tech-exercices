from random import *
from numpy import *
# Domino Game
# Saisie (n entiere pair et 4<=n<=56)
def saisie():
    n = int(input("donner n entiere pair et 4<=n<=56 : "))
    while not (n % 2 == 0 and 4 <= n <= 56):
        n = int(input("donner n entiere pair et 4<=n<=56 : "))
    return n
#Remp de tableau
def remp(T,n):
    for i in range(n):
        T[i]=int(input("donner T["+str(i)+"] : "))
        while not 0<=T[i]<=6:
            T[i]=int(input("donner T["+str(i)+"] : "))
    return T
#Verif
def verif(T,n):
    xD=True
    i=1
    while xD and i<n-3:
        if (T[i]!=T[i+1]):
            xD=False
        else:
            i+=2
    return xD
#Programme Principlae
n1=saisie()
T1=array([int]*n1)
remp(T1,n1)
if verif(T1,n1)==False:
    print("Le tableau est non valide")
else:
    print("Le tableau est valide")
for j in range(0,n1,2):
    print(T1[j],end="|")
