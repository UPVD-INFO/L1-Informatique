#TD4 Exo2

from math import cos

a= float(input("Entrer a: "))
b= float(input("Entrer b: "))
eps= float(input("Entrer eps: "))

while (abs(b-a)>eps):
    m = a + abs(b-a)/2
    if cos(a)*cos(m) == 0 :
        print("Gagne : x= ",m)
    elif cos(m)*cos(a) < 0:
        b= m
    else:
        a=m
    print("[a,b] : [",a,",",b,"]")
