'''ROle: Lire un entier n et afficher tout les i de 0 a n
Variables: n, i: entier
'''
##On procede a la lecture
n= int(input("Donnez moi n= "))

i= 0
while i<= n:
    print(i)
    i= i+1

n= int(input("Donnez moi n= "))

for i in range(0,n+1,1):
    print(i)
