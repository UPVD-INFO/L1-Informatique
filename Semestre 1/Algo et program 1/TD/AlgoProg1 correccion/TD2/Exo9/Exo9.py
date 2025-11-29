'''ROle: ecrire un programme qui lit une date et te sort le jour en utilisant if else
Variable:
f,j,m,a,m1,a1,ns,as: entier
semaine,jsemaine: liste
'''
#On demande les valeurs a calculer
j= int(input("Donne moi le jour= "))
m= int(input("Donne moi le mois= "))
a= int(input("DOnne moi l'annee= "))

#On commence le calcule
#On determine m1
if m>=3:
    m1= m-2
else:
    m1= m+10
#On determine a1
if m>=3:
    a1= a
else:
    a1= a-1
#On determine ns et ans
##a1= str(a1)
##ns= int(a1[:2])
##ans= int(a1[-2:])
##a1= int(a1) #On reconvertit a1 en entier
ns= a1//100
ans= a1 % 100

#On procede au calcul
f= j + ans + (ans//4) -2 * ns + (ns//4) + ((26*m1-2)//10)
f= f % 7

print(f"\n")
#On determine le jour
######################Solution 1###############################
##if f== 0:
##    print("Le jour est dimanche")
##elif f==1:
##    print("le jour est lundi")
##elif f==2:
##    print("le jour est mardi")
##elif f==3:
##    print("le jour est mercredi")
##elif f==4:
##    print("le jour est jeudi")
##elif f==5:
##    print("le jour est vendredi")
##elif f==6:
##    print("le jour est samedi")
####################Solution 2#################################
semaine = ["Dimanche","lundi","mardi","mercredi","jeudi","vendredi","samedi"]
jsemaine= f%7

print(f"Le jour de la semaine est {semaine[jsemaine]}")
