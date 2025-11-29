'''Écrire un programme qui affiche un rectangle d’étoiles plein, de largeur l et hauteur h.
Variables:
l,h,i,j: entier
'''
l= int(input("l= "))
h= int(input("h= "))

##i=0
##while i<h:
##    j=0
##    while j<l:
##        print("*",end="")
##        j+=1
##    print()
##    i+=1

for i in range(0,h,1):
    for j in range(0,l,1):
        print("*",end="")
    print()
