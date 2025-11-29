'''Écrire un programme qui affiche un triangle rectangle d’étoiles vide, de hauteur h et de base b. Le triangle
sera dans un premier temps afficher avec la base en bas.
Variable:
h,l,i,j: entier
'''


b= int(input("b= "))
h= int(input("h= "))


i=1
while i<=h:
    if i==h:
        j=1
        while j<=b:
            print("*",end="")
            j+=1
    if i>=1 and not(i==h):
        j= 1
        while j<=i:
            if j==1 or j==i:
                print(end="*")
            else:
                print(end=" ")
            j+=1
    i+=1
    print()


for i in range(1,h+1,1):
    if i==h:
        for j in range(1,b,1):
            print(end="*")
    if i>=1:
        for j in range(1,i+1,1):
            if j==1 or j==i:
                print(end="*")
            else:
                print(end=" ")
        
    print()
