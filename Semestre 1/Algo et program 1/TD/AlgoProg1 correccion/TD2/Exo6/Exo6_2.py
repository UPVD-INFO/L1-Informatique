'''Role: Lire une heure en minutes seconds heures et puis ajouter une heure et afficher les 3 resultat
Variables:
h,m,s,r,d,d2 entier
'''
h= int(input("Donnez moi l'heure= "))
m= int(input("Donnez moi les minutes= "))
s= int(input("Donnez moi les secondes= "))

print(f"Le temps actuel est de {h}:{m}:{s}")
print("On va rajouter une seconde")

s= s+1

if s>=60:
    s= 0
    m=m+1
if m>= 60:
    m= 0
    h= h+1

########################### Solution 1############################################
##if h== 24:
##    h= 0
########################## Solution 2###########################################
if h>= 24:
    h= h%24

print(f"{h}:{m}:{s}")
