'''Écrire un programme qui affiche une ligne de n étoiles.
Variables:
i,n: entier
'''
n= int(input("n= "))

i=0
while i<n:
    print("*",end="")
    i+=1
print()

##for i in range(0,n,1):
##    print("*",end="")
##print()
