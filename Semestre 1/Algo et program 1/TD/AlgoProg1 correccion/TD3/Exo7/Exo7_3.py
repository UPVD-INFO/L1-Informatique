'''Écrire un programme qui affiche un rectangle d’étoiles vide
Variables:
l,h,i,j: entier
'''

l= int(input("l ="))
h= int(input("h ="))

i=1
while i<=h:
    if i==1 or i==h:
        j=1
        while j<=l:
            print("*",end=" ")
            j+=1
    if i>1 and not(i==h):
        j=1
        while j<=l:
            if j==1 or j==l:
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
    i+=1
    print()

##for i in range(1,h+1,1):
##    if i==1 or i==h:
##        for j in range (1,l+1,1):
##            print("*",end="")
##            
##    if i>1 and not(i==h):
##        
##        for j in range(1,l+1,1):
##            if j==1 or j==l:
##                print("*",end="")
##            else:
##                print(end=" ")
##
##    print()

########################################
####Correcion prof#####
#Premiere ligne pleine
for l in range(largeur):
    print("*",end="")
print()
#Les lignes vides
for h in range(hauteur-2):
    #Pour chaque ligne
    print("*",end="")
    for l in range(largeur-2):
        print(" ",end="")
        
