#Version Mur int

L= int(input("L= "))
H= int(input("H= "))
l= int(input("l= "))
h= int(input("h= "))

if H%h!=0 or (L-l/2 !=0) :
    print("Les valeurs ne verifient pas les hypotheses")
else:
    nb_briques= 0
    hcur=0
    while hcur< H: #while hcur!=H:
        #Calculer pour la ligne
        lcur=0
        while lcur<L: #while lcur !=0:
            nb_vriques +=1
            lcur +=1
        hcur +=h
    print("NB briques: ", nb_briques)

#version mur float

L= int(input("L= "))
H= int(input("H= "))
l= int(input("l= "))
h= int(input("h= "))


nb_briques= 0
hcur=0
while hcur< H: #while hcur!=H:
    #Calculer pour la ligne
    lcur=0
    while lcur<L: #while lcur !=0:
        nb_vriques +=1
        lcur +=1
    hcur +=h
    print("NB briques IT: ", nb_briques)

nb_briques= (((L-l)/2)/l) * (H/h)
print("NB briques=",nb_briques)

L= int(input("L= "))
H= int(input("H= "))
l= int(input("l= "))
h= int(input("h= "))

##nb_briques= (int(((L-l)/2)/l) + 1) * int((H/h) + 1)
if (int(H/h))/(H/h)==1:
    nb_briques= (int(((L-l)/h)/l) + 0) * int((H/h) + 0)
else:
    nb_briques= (int(((L-l)/h)/l) + 1) * int((H/h) + 1)
print("NB briques superieur: ",nb_briques)
