'''Role: Lire une heure en minutes seconds heures et puis ajouter une heure et afficher les 3 resultat
Variables:
h,m,s,r,d entier
'''

h= int(input("Quel est l'heure?\n"))
m= int(input("COmbien de minutes= "))
s= int(input("Combien de secondes= "))

print(f"Le temps actuel est {h}:{m}:{s}")
print("On rajoute une seconde")

#On passe par la phase de secondes
d= h*3600
d= d+(m*60)
d= d+s

#On retourne au debut en rajoutant un 1
d= d+1
h= d//3600
r= d%3600
m= r//60
s= r%60

###################################### Solution 1 ###############################################
##if h== 24:
##    h= 0
##    print(f"{h}:{m}:{s}")
##else:
##    print(f"{h}:{m}:{s}")

###################################### Solution 2 ###############################################
##
##if h== 24:
##    h= 0

###################################### Solution 3 ###############################################

h = h % 24

print(f"{h}:{m}:{s}")
