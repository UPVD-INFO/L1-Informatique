'''Role: Lire n et calculer la valeur d'argent le lendemain du n-eme anniversaire
Variables: n, somme_d,somme_i, double_a, total_d: entier
'''

n= int(input("Donnez moi n= "))

#vesion while
i= 1
somme_a= 100
while i <= n:
    somme_a= somme_a + 15 + (i*2)
    i= i+1
print("la somme d'argent le lendemain es de ",somme_a)


#version for in range
somme_a= 100
for i in range(1,n+1,1):
    somme_a= somme_a + 15 + (i*2)
print("la somme d'argent le lendemain es de ",somme_a)

#version sans iteratives

f= 100+(15*n + n*(n+1))
print("la somme d'argent le lendemain es de ", f)
