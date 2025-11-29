from random import randint
a= randint(0,100)

print(a)
i=0

while i<5:
    ans= int(input("ans= "))
    if ans==a:
        print("Bravo, Vous avez trouve la bonne reponse")
        i= i+5
    elif ans<a:
        print("le nombre saisie est inferieur au nombre recherche")
    else:
        print("le nombre saisie est superieur au nombre recherche")
    i+=1
    
if i==5:
    print("VOus avez perdu")

###version ameliore
i=0
ans=0
while i<5 and ans!=a:
    ans= int(input("ans= "))
    if ans<a:
        print("le nombre saisie est inferieur au nombre recherche")
    elif ans>a and ans!=a:
        print("le nombre saisie est superieur au nombre recherche")
    i+=1
    
if ans==a:
    print("VOus avez gagne")
else:
    print("Perdu")

n=int(input("n:"))
f0=0
f1=1
for i in range(0,n+1):
    t=f0
    f0=f0+f1
    f1=t
print(f1)
