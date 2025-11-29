#Role: Avoir la temperature en C la passer en F et puis les comparer
#Variables:
#C réel
#F réel

C=float(input("Quel est la temperature en Celsius\n"))
F= (9/5)*C+32

if C > F:
    print("La valeur", "{:.1f}".format(C), "en degrée Celsius est plus grande que", "{:.1f}".format(F), "en degrée Farenheit")
if C < F:
    print("La valeur", "{:.1f}".format(C),"en degrée Celsius est plus petite que", "{:.1f}".format(F)," en degrée Farenheit") #On compare puis on affiche le resultat
if C == F:
    print("La valeur", "{:.1f}".format(C)," en degrée Celsius est egalle a", "{:.1f}".format(F)," en degrée Farenheit")
