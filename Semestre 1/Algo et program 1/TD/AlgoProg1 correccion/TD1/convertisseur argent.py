#Role: Lire une somme en dollars, la convertir en euros puis l'afficher
#Variables: somme-dollars, somme euros,taux: rel/float

somme_dollars= int(input("Quel est la quantite de dolar?\n"))
taux= 0.6604
somme_euros= taux*somme_dollars

print("La somme en euros est de", somme_euros)
