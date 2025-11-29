'''Role: Savoir si une année est bisextile en utilisant des operateurs logiques
Variables:
annee, a1,a2: entier
'''
from math import *

annee = int(input("Quel est l'annee= "))

while annee < 1582:
    print("l'annee ne peut pas etre calcule")

    annee = int(input("Quel est l'annee= "))
    
#Savoir si l'annee est bisextile ou non
    
if (annee % 4) == 0 and (annee % 100) != 0 or (annee % 400) == 0:
    print(f"l'annee {annee} est bisextile")
else:
    print(f"l'annee {annee} n'est pas bisextile")

    # On determine la prochaine annee bisextile
    a1= annee
    a2= annee

    while not((a1 % 4) == 0 and (a1 % 100) != 0 or (a1 % 400) == 0):
         a1 = a1 + 1
    while not((a2 % 4) == 0 and (a2 % 100) != 0 or (a2 % 400) == 0):
        a2= a2 - 1

    if abs(a1-annee)< abs(a2-annee):
        print(f"l'annee la plus proche {a1}")
    elif abs(a1-annee) > abs(a2-annee):
        print(f"l'annee la plus proche {a2}")
    elif abs(a1-annee) == abs(a2-annee):
        print(f"les annees les plus proches sont {a1} et {a2} ")
