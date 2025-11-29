'''Role: Creer le jeu de l'awale
Variables:
    g1,g2,cases_p,gr: entier
    t[][]: tab 2d entier
    cases_v,j1,j2: boleeen
'''
#Creation de la grille de jeu
##n= int(input("nj= "))
t=[[4 for col in range(6)]for lig in range(2)]

for lig in range(2):
    for col in range(6):
        print(t[lig][col],end=" ")
    print()


cases_v= False #cases vides
cases_p= 0 #cases avec des grains
joueur= 1
g1=0 #recolte de grains joueur 1
g2=0 #meme chose joueur 2


while cases_v == False:
    #Demande l'utilisateur de prendre des grains
    lig= int(input("Dans quel ligne voulez prendre les grains= "))
    col= int(input("Dans quel cologne voulez prendre les grains= "))
    gr= t[lig][col] #grains recoltes
    t[lig][col]=0
    i=1
    while gr>0:
        if lig==1 and col<5:
            col+=i
            t[lig][col]+=1
            gr-=1
        if lig==1 and col==5:
            col-=i
            t[0][col]+=1
            gr-=1
        ####
        if lig==0 and col>0:
            col-=i
            t[0][col]+=1
            gr-=1
        if lig==0 and col==0:
            col+=i
            t[1][col]+=1
            gr-=1
        
    #Affichage de la grille de jeu
    for lig in range(2):
        for col in range(6):
            print(t[lig][col],end=" ")
        print()          
#Detecteur de graines sur le tableau
##for lig in range(2):
##    for col in range(6):
##        if t[lig][col]>0:
##            cases_p+=1
##if cases_p==0:
##    cases_v= True

