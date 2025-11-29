'''Écrire un programme qui affiche un rectangle d’étoiles vide
Variables:
l,h,i,j: entier
'''

l= int(input("l ="))
h= int(input("l ="))

i=1
while i<=n:
    if i==1:
        j=0
        while j<n:
            print("*",end="")
            j+=1
    if i>1:
        j=0
        print("*",end="")
        while j<n:
            print(" ",end="")
        print("*",end="")
    if i==n:
        j=0
        while j<n:
            print("*",end="")
            j+=1
    print()
