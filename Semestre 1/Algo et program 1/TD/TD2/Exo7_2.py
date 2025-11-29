'''Role: Savoir si une année est bisextile en utilisant des operateurs logiques
Variables:
annee: entier
'''

annee = int(input("Quel est l'annee= "))

#Savoir si l'annee est bisextile ou non
if (annee % 4) == 0 and (annee % 100) != 0 or (annee % 400) == 0:
    print(f"l'annee {annee} est bisextile")
else:
    print(f"l'annee {annee} est pas bisextile")


