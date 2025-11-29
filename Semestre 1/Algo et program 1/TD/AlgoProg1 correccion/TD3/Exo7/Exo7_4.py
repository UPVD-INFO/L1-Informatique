'''Écrire un programme qui affiche un triangle rectangle d’étoiles vide, de hauteur h et de base b. Le triangle
sera dans un premier temps afficher avec la base en haut.
Variables:
h,b,i,j: entier
'''
##b= int(input("b= "))
##h= int(input("h= "))

##########Solution 1 pour triangle remplis####################
##i=1
##while i<=h:
##    j=1
##    while j<=b:
##        print("*",end="")
##        j+=1
##    i+=1
##    b-=1
##    print()

#########Version Avec le calcul de x##########
##x/b= (i-j)/h
##x= b(i-j)/h
##b= j  h= i
##for i in range(1,h+1,1):
##    for j in range(1,b+1,1):
##        x= b*(i-j)//i
##        for l in range(1,x+1):
##            print("*",end=" ")
##    print()
##i=1
##while i<=h:
##    if i==1:
##        j=0
##        while j<=b:
##            print("*",end="")
##            j+=1
##    if i>1:
##        j= 1
##        while j<=b:
##            if j==1 or j==b:
##                print(end="*")
##            else:
##                print(end=" ")
##            j+=1
##        b-=1
##    i+=1
##    print()

# faut faire que la base= hauteur
##for i in range(1,h+1,1):
##    if i==1:
##        for j in range(0,b+1,1):
##            print(end="*")
##    if i>1:
##        for j in range(1,b+1,1):
##            if j==1 or j==b:
##                print(end="*")
##            else:
##                print(end=" ")
##        b-=1
##    print()


######################correction prof###############################
from math import ceil

b= int(input("b= "))
h= int(input("h= "))

print("triangle plein normal")
for l in range(0,h):
    nbe= ceil((b*(h-l))/h)
    for c in range(1,nbe+1):
        print(c,end=" ")
    print()
print()
############################ Pour le vide(moi)######################
#l=(hauteur) et c (base)

print("triangle vide normal")
for l in range(0,h):
    nbe= ceil((b*(h-l))/h)
    for c in range(1,nbe+1):
        if l==0 or c==1 or c==nbe:
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
##########################triangle inverse#############################

print("triangle plein inverse")
for l in range(h-1,-1,-1):
    nbe= ceil((b*(h-l))/h)
    for c in range(nbe,0,-1):
         if l==0 or c==1 or c==nbe:
            print("*",end="")
         else:
            print(end=" ")
    print()
print()
##trouver moyen pour pas changer les conditions

