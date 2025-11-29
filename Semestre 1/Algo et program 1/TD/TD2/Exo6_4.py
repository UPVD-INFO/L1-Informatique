'''ROle: Lire une heure et ajouter une seconde (ou retrancher) puis afficher la
nouvelle heure
Variables:
heure,minutes,secondes : entier
'''

heure = int(input("Quel est l'heure= "))
minutes = int(input("Combien de minutes= "))
secondes = int(input("COmbien de secondes= "))

print(f"{heure}:{minutes}:{secondes}")
#On rajoute une seconde
secondes = secondes + 1

#On recalcule l'heure
minutes = minutes + secondes // 60
secondes = secondes % 60
heure = heure + minutes // 60
minutes = minutes % 60
heure = heure % 24

print(f"{heure}:{minutes}:{secondes}")


    
