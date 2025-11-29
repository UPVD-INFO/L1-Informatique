'''Role: Lire n et afficher i au care
Variables: n,i: entier
'''

#On procede a lire
n= int(input("Donnez moi n= "))

##i= 0
##j= 0
##while i<= n:
##    j= i**2
##    print(j)
##    i= i+1
    
i= 0
while i<= n:
    print(i**2)
    i= i+1


n= int(input("Donnez moi n= "))

for i in range(0,n+1,1):
##    j= i**2
##    print(j)
    print(i**2)
