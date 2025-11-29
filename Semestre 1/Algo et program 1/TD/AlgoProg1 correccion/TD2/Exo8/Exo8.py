'''ROle: Lire un numero de securite sociale et sa cle puis afficher si la cle est correct
Variables:
secu: chaine de caractere
cle, numero, secu, verif: entier
'''
############################# Solution 1 ########################################
##secu= int(input("Donne moi ton numero de securite sociale= "))
##cle = 97 - (secu % 97)
##print(cle)
##print("ta cle de securite sociale est vrai")

############################# Soluion 1 #########################################
#On verifie les valeurs rentrant
secu= str(input("Donne moi ton muero de securite sociale= "))
while len(secu) != 13:
    print("le numero donne n'est pas valide")
    secu= str(input("Donne moi ton numero de securite sociale= "))

cle= str(input("Donne moi ta cle= "))    
while len(cle) !=2:
    print("La cle donne n'est pas valide")
    cle= str(input("Donne moi ta cle= "))
    
#On verifie si la cle est correcte
numero= int(secu)
cle= int(cle)
verif= 97 - (numero % 97)

if verif == cle:
    print("la cle est correcte")
else:
    print("la cle n'est pas correcte")

############################ SOlution 3 #########################################

##secu= str(input("Donne moi ton numero de securite sociale= "))
##
##while len(secu) != 15:
##    print("le numero donne n'est pas valide")
##    secu= str(input("Donne moi ton numero de securite sociale= "))
##    
##numero = int(secu[:13])
##cle = int(secu[-2:])
##verif = (97 - (numero % 97))
##if verif == cle:
##    print("Le numero de securite sociale est valide")
##
##else:
##    print("le numero donne n'est pas valide")
    

