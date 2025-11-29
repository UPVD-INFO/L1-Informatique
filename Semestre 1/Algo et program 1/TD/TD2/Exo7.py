'''ROle: Calculer une année et voir si elle est bisextile ou non sans operateurs
logiques.
Variables:
annee: entier
'''

annee = int(input("Quel est l'annee= "))

while annee < 1582:
    print("l'annee ne peut pas etre calcule")

    annee = int(input("Quel est l'annee= "))

#On calcule l'annee bisextile

if (annee % 4) == 0:
    if (annee % 100) != 0:
        print(f"l'annee {annee} est bisextile")
if (annee % 400) == 0:
    print(f"l'annee {annee} est bisextile")
else:
    print("l'annee est pas bisextile")
