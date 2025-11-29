'''Role: Lire une heure en minutes seconds heures et puis ajouter une heure et afficher les 3 resultat
Variables:
h,m,s,n entier
'''

h= int(input("Quel est l'heure?\n"))
m= h*60
s= m*60

print("h=",h,"\nm=",m,"\ns=",s)
n= int(input("\nCombien de secondes tu veut rajouter?"))

s= s+n
m= s/60
h= m/60

print("\nLa nouvelle heure est de h=","{:.2f}".format(h),"\nm=","{:.2f}".format(m),"\ns=",s)


