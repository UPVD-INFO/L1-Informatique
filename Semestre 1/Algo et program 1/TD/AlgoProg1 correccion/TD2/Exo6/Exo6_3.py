'''Role: Lire une heure en minutes seconds heures et puis retrancher seconde et affiche la nouvelle heure
Variables:
h,m,s,r,d,d2 entier
'''
h= int(input("Donnez moi l'heure= "))
m= int(input("Donnez moi les minutes= "))
s= int(input("Donnez moi les secondes= "))

print(f"Le temps actuel est de {h}:{m}:{s}")
print("On va rajouter une seconde")

s= s-1

if s== -1:
    s= 59
    m= m-1
if m== -1:
    m= 59
    h= h-1
############################### Solution 1 ################################################
##if h== -1:
##    h= 23

############################### Solution 2 ################################################

h= h%24

print(f"{h}:{m}:{s}")
