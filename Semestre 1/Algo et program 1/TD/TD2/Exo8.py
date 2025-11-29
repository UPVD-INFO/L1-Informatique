'''ROle: Lire un numero de securite sociale et afficher la cle correct
Variables:
secu: chaine de caractere
cle, numero: entier
'''
############################# Solution 1 ########################################
##secu= int(input("Donne moi ton numero de securite sociale= "))
##cle = 97 - (secu % 97)
##print(cle)
##print("ta cle de securite sociale est vrai")

############################# Soluion 1 #########################################

##secu= int(input("Donne moi ton muero de securite sociale= "))
##cle= int(input("Donne moi ta cle= "))
##
##if (97 - (secu % 97) == cle):
##    print("la cle est vrai")
##
##else:
##    print("la cle est fausse")

############################ SOlution 3 #########################################

secu= str(input("Donne moi ton numero de securite sociale= "))

while len(secu) != 15:
    print("le numero donne n'est pas valide")
    secu= str(input("Donne moi ton numero de securite sociale= "))
    
numero = int(secu[:13])
cle = int(secu[-2:])
verif = (97 - (numero % 97))
if verif == cle:
    print("Le numero de securite sociale est valide")

else:
    print("le numero donne n'est pas valide")
    

