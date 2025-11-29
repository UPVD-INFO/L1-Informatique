'''Role: Lire n au clavier et determiner la table de produit i*j si n>0
Variables: n,i,j,p: entier
            tab_m: tableau
'''

n= int(input("n= "))

##if n > 0:
##    i=0
##    j=0
##    while i<=n:
##        while j<=n:
##            p=i*j
##            print(p,end="")
##            j=j+1
##            i=i+1
##            if i<=n or j<=n:
##                print(",",end="")
##    print(".",end="")
##
##else:
##    print("Erreur")

##if n > 0:
##    j=0
##    for i in range(0,n+1,1):
##       p=i*j
##       print(p,end="")
##       j+=1
##       if i<n or j<n:
##           print(",",end="")
##    print(".",end="")
##
##else:
##    print("Erreur")


##if n > 0:
##    l=str(n*n)
##    i=0
##    while i<=n:
##        j=0
##        while j<=n:
##            r= str(i*j)
##            while len(r)<len(l):
##              r= r+" "
##            print(r,end=" ")
##            j+=1
##        print()
##        i+=1
##
####    l= str(n*n)
####    for i in range(0,n+1,1):
####        for j in range(0,n+1,1):
####            r= str(i*j)
####            while len(r)<len(l):
####                r= r + " "
####            print(r,end=" ")
####        print()
##else:
##    print("Erreur")

##largmax= len(str(n*n)
##for i in range(n+1):
##             for j in range(n+1):
##                 larg= len(str(n*n)
##                 for z in range(largemax-larg):
##                     print(" ",end="")
##                 print(l*c,end="")
##             print()
##print()

largmax= len(str(n*n))
for i in range(n+1):
    for j in range(n+1):
        print(str(i*j).rjust(largmax),end="")
    print()
print()
