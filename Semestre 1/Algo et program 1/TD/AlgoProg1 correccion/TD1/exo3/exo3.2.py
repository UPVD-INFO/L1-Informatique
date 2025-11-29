'''ROle: Faire une permutation circulaire avec une seule variable intermediaire

Variables: X1, X2, X3, I'''

from math import *

X1= int(input("Quel est la valeur de X1?\n"))
X2= int(input("Quel est la valeur de X2?\n"))
X3=int(input("Quel est la gvaleur de X3?\n"))
#On va mtn changer les valeurs

print("Valeur au debut", X1,X2,X3)

X1=X1+X2+X3
X2=X1-X2-X3
X3=X1-X2-X3
X1=X1-X2-X3


 
print("Valeur de fin", X1,X2,X3)


