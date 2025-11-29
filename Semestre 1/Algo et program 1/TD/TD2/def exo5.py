#Role: montrer le prix d'un obnjet HT et TTC
#Variables:
#HT float
#TTC float
#Taxe float


HT= float(input("Quel est le prix de l'objet hors taxe?\n")) 
Taxe= 1.206 #Ici on demande la valeur et puis on passe au calcul 
TTC= HT*Taxe

print("Le prix de l'objet avec TTC est de", "{:.2f}".format(TTC))


#Role: Detecter si un chiffre est posivite nulle ou negative
#Variables:
#C entier

C= int(input("Donne moi le chiffre=\n"))# On demande a saisir le chiffre

if C==0:
    print("Le chiffre donnée est nulle") #Si le chiffre est nulle alors le programme s'arrete ici

else:            #Sinon le programme continue et maintenant cherchera a savoir si le chiffre est soit positive ou soit nulle
    if C>0:
        print("Le chiffre donnée est positive")
    else:
        print("Le chiffre donnée est negative")
    
