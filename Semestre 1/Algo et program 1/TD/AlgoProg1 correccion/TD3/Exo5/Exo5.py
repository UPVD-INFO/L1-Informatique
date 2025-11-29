'''Role: Ecrire un programme qui verifie si un entier n est egal a la somme de ses diviseurs
Variables: i,n: enier
'''
n= int(input("n= "))

##i= 1
##s= 0
##while i<n:
##    if n%i == 0:
##        s= s+i
##    i= i+1

s=0
for i in range(1,n,1):
    if (n%i) == 0:
        s= s+i

if n == s:
    print(n," est un nombre parfait")
else:
    print(n," n'est pas un nombre parfait")
