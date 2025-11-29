#Role: Convertiisseur prix HT en TTC
#Variables: HT,TTC,taxe: réel/float.

from math import *

HT= float(input("Quel est le prix de l'objet?\n"))
taxe=1.206
TTC=HT * taxe

print("Le prix avec taxe est de", TTC)
print("{:3.2f}".format(TTC))
