'''ROle: Créer un programme qui demande une heure et qui retranche 1 sec puis affiche la nouvelle heure
Variables:
h,m,s entier
'''
#Demande l'heure
h= int(input("Donnez moi l'heure"))
m= int(input("Donnez moi les minutes"))
s= int(input("Donnez moi les secondes"))

print(f"{h}:{m}:{s}")

############################################### Solution 1 #####################################################
###On retranche 1 seconde
##s= s-1
##d= (h*3600)+(m*60)+s
##
###On retourne aux heures
##h= d//3600
##r= d%3600
##m= r//60
##r= r%60
##s= r%60
##
##h= h%24

############################################### Solution 2 #####################################################
s= s-1

if s== -1:
    m= m-1
    s= 59
if m== -1:
    h= h-1
    m= 59
if h== -1:
    h= 23
    
#Solution 1 pour les heures
##h= h%24

#On affiche le resultat
print(f"{h}:{m}:{s}")

