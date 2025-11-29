'''Role: Demander a l'utilisateur combien de photocopie vaut faire et faire et afficher le calcul correspondant selon la reponse et le nombre de photocopie effectue
Variables:
n,c entier
'''

n= int(input("Combien de photocopies vouleez faire?\n")) #On demande les variables

if n <= 10:
    c= n*5
    print("Le nombre de photocpie est de", n," et la facture est de", c)
else:
    if n <=20:
        c= n*3      
        print("Le nombre de photocopie est de", n," et la facture est de", c)
    else:
        c= n*1.5
        print("Le nombre de photocopie est de", n," et la facture est de", c)
