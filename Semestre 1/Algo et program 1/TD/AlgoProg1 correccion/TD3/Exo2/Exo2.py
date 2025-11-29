'''Role: ecrire un programme qui lit des entiers et qui deroule la multiplication egyptienne
Variables: a,b,r
'''

#On procede a la lecture
a= int(input("Donnez moi a= "))
b= int(input("Donnez moi b= "))

r= 0
while b != 0:
    if (b%2) == 0:
        a= a*2
        b= b/2
    else:
        b= b-1
        r= a+r
print(r)
