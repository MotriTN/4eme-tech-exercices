from numpy import *


def inputting():
    global N
    N = int(input("Donner la taille de tableau: "))
    while not (1 <= N <= 9):
        N = int(input("Donner la taille de tableau: "))
    return N


inputting()


def Verify_Input(nom):
    Is_Good = False
    if (3 <= len(nom) <= 20):
        Is_Good = True
        i = 0
        while i < len(nom) and Is_Good == True:
            if 65 <= ord(nom[i]) <= 88:
                Is_Good = False
            i += 1
    return Is_Good


T = array([N * str])


def remp1(T, N):
    global nom
    nom = input("Donner Votre Nom: ")
    for i in range(N):
        while not Verify_Input(nom) == True:
            nom = input("Donner Votre Nom: ")
        T[i] = nom
    return T


remp1(T, N)


def Voy(nom):
    for i in range(len(nom)):
        voyel = "OIYEAU"
        nb = 0
        if voyel.find(nom[i]) != -1:
            nb += 1
    return nb


def mot_de_passe(nom):
    global mot_de_passe
    mot_de_passe = nom[:2]


Tid = array([N * str])
