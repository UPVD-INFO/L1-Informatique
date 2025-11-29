#Role: Calculer la vitesse moyenne
#Variables: D,T,H,V.

D=int(input("Quel est la distance parcourue?\n"))
T=int(input("Quel est le temps en total?\n"))
H=T/60
V=D/H

print("La vitesse moyenne est de", V)
