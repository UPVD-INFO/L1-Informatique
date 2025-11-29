'''Écrire un programme qui imprime un triangle rectangle pour n un entier lu au clavier.
Variables: i,j,n: entier
'''

n= int(input("n= "))

##i= 1
##while i<=n:
##    j=1
##    while j<=i:
##        print(j,end=" ")
##        j+=1
##    print()
##    i+=1

for i in range(0,n+1,1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
    

