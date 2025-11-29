'''Role: Demander une heure retrancher une seconde puis afficher la nouvelle heure
Variables:
heure,minutes,secondes entier
'''
heure= int(input("Quelle est l'heure= "))
minutes= int(input("Combien de minutes= "))
secondes= int(input("Combien de secondes= "))

#On retranche 1 seconde
secondes= secondes+1



print(f"{heure}:{minutes}:{secondes}")
