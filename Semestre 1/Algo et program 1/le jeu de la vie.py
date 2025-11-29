#Le jeu de la vie
from random import randint

n= int(input("n= "))
graphe=[[False for col in range(n)]for lig in range(n)]

#Affichage de la grille
for lig in range(n):
    for col in range(n):
        print("----",end="")
    print("-")
    for col in range(n):
        if graphe[lig][col]==False:
            print("| .",end=" ")
        else:
            print("| X",end=" ")
    print("|")
for col in range(n):
        print("----",end="")
print("-")

#Sans randint
#Choix nombres cellules vivantes
coups= int(input("COmbien de cellule vivante voulez vous mettre dans la grille= "))

while coups > 0:
    #Lecture coordonnees cellule vivante et affichage
    lig= int(input("Dans quel ligne voulez placer la cellule= "))
    col= int(input("Dans quel cologne voulez placer la cellule= "))
    graphe[lig][col]= True
    coups-=1
    for lig in range(n):
        for col in range(n):
            print("----",end="")
        print("-")
        for col in range(n):
            if graphe[lig][col]==False:
                print("| .",end=" ")
            else:
                print("| X",end=" ")
        print("|")
    for col in range(n):
            print("----",end="")
    print("-")
#Verification conditions cellules
cycle= int(input("Combien de cycle voulez vous faire= "))
cel_V= True
ligne=0
cologne=0
while cel_V==True and cycle>0:
    total_cel_V=0
    #Verification cellule Vivante
    if graphe[ligne][cologne]==True:
        #Verification Bord du haut
        if ligne==0 and cologne>0 and cologne<n-1:
            #Verification des alentours de la cellule vivante
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne+1] == True:
                total_cel_V+=1
            if total_cel_V<2 or total_cel_V>3:
                graphe[ligne][cologne]= False
        #Verification Bord du bas
        if ligne==n-1 and cologne>0 and cologne<n-1:
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne+1] == True:
                total_cel_V+=1
            if total_cel_V<2 or total_cel_V>3:
                graphe[ligne][cologne]= False
        #Verification Bord de droit
        if cologne==n-1 and ligne>0 and ligne<n-1:
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne-1] == True:
                total_cel_V+=1
            if total_cel_V<2 or total_cel_V>3:
                graphe[ligne][cologne]= False
        #Verification Bord de gauche
        if cologne==0 and ligne>0 and ligne<n-1:
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne+1] == True:
                total_cel_V+=1
            if total_cel_V<2 or total_cel_V>3:
                graphe[ligne][cologne]== False
        #Verification angle droit haut
        if ligne==0 and cologne==n-1:
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne-1] == True:
                total_cel_V+=1
            if total_cel_V<2 or total_cel_V>3:
                graphe[ligne][cologne]= False
        #Verification angle droit bas
        if ligne==n-1 and cologne==n-1:
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne-1] == True:
                total_cel_V+=1
            if total_cel_V<2 or total_cel_V>3:
                graphe[ligne][cologne]= False
        #Verification angle gauche haut
        if ligne==0 and cologne==0:
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne+1] == True:
                total_cel_V+=1
            if total_cel_V<2 or total_cel_V>3:
                graphe[ligne][cologne]= False
        #Verification angle gauche bas
        if ligne==n-1 and cologne==n-1:
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne+1] == True:
                total_cel_V+=1
            if total_cel_V<2 or total_cel_V>3:
                graphe[ligne][cologne]= False
        #Verification milieu du graphe
        if ligne>0 and ligne<n-1 and cologne>0 and cologne<n-1:
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne-1] == True:
                total_cel_V+=1
            if total_cel_V<2 or total_cel_V>3:
                graphe[ligne][cologne]= False
    #Verification cellule  morte 
    else:
        #Verification Bord du haut
        if ligne==0 and cologne>0 and cologne<n-1:
            #Verification des alentours de la cellule vivante
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne+1] == True:
                total_cel_V+=1
            if total_cel_V==3:
                graphe[ligne][cologne]= True
        #Verification Bord du bas
        if ligne==n-1 and cologne>0 and cologne<n-1:
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne+1] == True:
                total_cel_V+=1
            if total_cel_V==3:
                graphe[ligne][cologne]= True
        #Verification Bord de droit
        if cologne==n-1 and ligne>0 and ligne<n-1:
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne-1] == True:
                total_cel_V+=1
            if total_cel_V==3:
                graphe[ligne][cologne]= True
        #Verification Bord de gauche
        if cologne==0 and ligne>0 and ligne<n-1:
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne+1] == True:
                total_cel_V+=1
            if total_cel_V==3:
                graphe[ligne][cologne]== True
        #Verification angle droit haut
        if ligne==0 and cologne==n-1:
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne-1] == True:
                total_cel_V+=1
            if total_cel_V==3:
                graphe[ligne][cologne]= True
        #Verification angle droit bas
        if ligne==n-1 and cologne==n-1:
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne-1] == True:
                total_cel_V+=1
            if total_cel_V==3:
                graphe[ligne][cologne]= True
        #Verification angle gauche haut
        if ligne==0 and cologne==0:
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne+1] == True:
                total_cel_V+=1
            if total_cel_V==3:
                graphe[ligne][cologne]= True
        #Verification angle gauche bas
        if ligne==n-1 and cologne==n-1:
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne+1] == True:
                total_cel_V+=1
            if total_cel_V==3:
                graphe[ligne][cologne]= True
        #Verification milieu du graphe
        if ligne>0 and ligne<n-1 and cologne>0 and cologne<n-1:
            if graphe[ligne+1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne] == True:
                total_cel_V+=1
            if graphe[ligne][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne+1][cologne-1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne+1] == True:
                total_cel_V+=1
            if graphe[ligne-1][cologne-1] == True:
                total_cel_V+=1
            if total_cel_V==3:
                graphe[ligne][cologne]= True
    #Affichage de la grille
    for lig in range(n):
        for col in range(n):
            print("----",end="")
        print("-")
        for col in range(n):
            if graphe[lig][col]==False:
                print("| .",end=" ")
            else:
                print("| X",end=" ")
        print("|")
    for col in range(n):
            print("----",end="")
    print("-")
    print("DEBUG: total_cel_V=",total_cel_V)
    cologne+=1  
    if cologne==n:
        cologne=0
        ligne+=1
    cycle-=1
        
    #Verification graphe
    cellules_mortes=0
    for lig in range(n):
            for col in range(n):
                if graphe[lig][col] == False:
                    cellules_mortes+=1
    if cellules_mortes==n*n:
            cel_V=False

#Avec randint
#Selection des donnees
##ncelV= randint(1,n*n)
##print(ncelV)
##for i in range(ncelV):
##    ligne= randint(0,n-1)
##    cologne= randint(0,n-1)
##    graphe[ligne][cologne]= True
##    print(ligne, cologne)
##    
##for lig in range(n):
##    for col in range(n):
##        print("----",end="")
##    print("-")
##    for col in range(n):
##        if graphe[lig][col]==False:
##            print("| .",end=" ")
##        else:
##            print("| X",end=" ")
##    print("|")
##for col in range(n):
##        print("----",end="")
##print("-")
##
###Verification conditions cellules
##cycle= int(input("Combien de cycle voulez vous faire= "))
##cel_V= True
##ligne=0
##cologne=0
##while cel_V==True and cycle>0:
##    total_cel_V=0
##    #Verification cellule Vivante
##    if graphe[ligne][cologne]==True:
##        #Verification Bord du haut
##        if ligne==0 and cologne>0 and cologne<n-1:
##            #Verification des alentours de la cellule vivante
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne+1] == True:
##                total_cel_V+=1
##            if total_cel_V<2 or total_cel_V>3:
##                graphe[ligne][cologne]= False
##        #Verification Bord du bas
##        if ligne==n-1 and cologne>0 and cologne<n-1:
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne+1] == True:
##                total_cel_V+=1
##            if total_cel_V<2 or total_cel_V>3:
##                graphe[ligne][cologne]= False
##        #Verification Bord de droit
##        if cologne==n-1 and ligne>0 and ligne<n-1:
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne-1] == True:
##                total_cel_V+=1
##            if total_cel_V<2 or total_cel_V>3:
##                graphe[ligne][cologne]= False
##        #Verification Bord de gauche
##        if cologne==0 and ligne>0 and ligne<n-1:
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne+1] == True:
##                total_cel_V+=1
##            if total_cel_V<2 or total_cel_V>3:
##                graphe[ligne][cologne]== False
##        #Verification angle droit haut
##        if ligne==0 and cologne==n-1:
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne-1] == True:
##                total_cel_V+=1
##            if total_cel_V<2 or total_cel_V>3:
##                graphe[ligne][cologne]= False
##        #Verification angle droit bas
##        if ligne==n-1 and cologne==n-1:
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne-1] == True:
##                total_cel_V+=1
##            if total_cel_V<2 or total_cel_V>3:
##                graphe[ligne][cologne]= False
##        #Verification angle gauche haut
##        if ligne==0 and cologne==0:
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne+1] == True:
##                total_cel_V+=1
##            if total_cel_V<2 or total_cel_V>3:
##                graphe[ligne][cologne]= False
##        #Verification angle gauche bas
##        if ligne==n-1 and cologne==n-1:
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne+1] == True:
##                total_cel_V+=1
##            if total_cel_V<2 or total_cel_V>3:
##                graphe[ligne][cologne]= False
##        #Verification milieu du graphe
##        if ligne>0 and ligne<n-1 and cologne>0 and cologne<n-1:
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne-1] == True:
##                total_cel_V+=1
##            if total_cel_V<2 or total_cel_V>3:
##                graphe[ligne][cologne]= False
##    #Verification cellule  morte 
##    else:
##        #Verification Bord du haut
##        if ligne==0 and cologne>0 and cologne<n-1:
##            #Verification des alentours de la cellule vivante
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne+1] == True:
##                total_cel_V+=1
##            if total_cel_V==3:
##                graphe[ligne][cologne]= True
##        #Verification Bord du bas
##        if ligne==n-1 and cologne>0 and cologne<n-1:
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne+1] == True:
##                total_cel_V+=1
##            if total_cel_V==3:
##                graphe[ligne][cologne]= True
##        #Verification Bord de droit
##        if cologne==n-1 and ligne>0 and ligne<n-1:
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne-1] == True:
##                total_cel_V+=1
##            if total_cel_V==3:
##                graphe[ligne][cologne]= True
##        #Verification Bord de gauche
##        if cologne==0 and ligne>0 and ligne<n-1:
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne+1] == True:
##                total_cel_V+=1
##            if total_cel_V==3:
##                graphe[ligne][cologne]== True
##        #Verification angle droit haut
##        if ligne==0 and cologne==n-1:
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne-1] == True:
##                total_cel_V+=1
##            if total_cel_V==3:
##                graphe[ligne][cologne]= True
##        #Verification angle droit bas
##        if ligne==n-1 and cologne==n-1:
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne-1] == True:
##                total_cel_V+=1
##            if total_cel_V==3:
##                graphe[ligne][cologne]= True
##        #Verification angle gauche haut
##        if ligne==0 and cologne==0:
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne+1] == True:
##                total_cel_V+=1
##            if total_cel_V==3:
##                graphe[ligne][cologne]= True
##        #Verification angle gauche bas
##        if ligne==n-1 and cologne==n-1:
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne+1] == True:
##                total_cel_V+=1
##            if total_cel_V==3:
##                graphe[ligne][cologne]= True
##        #Verification milieu du graphe
##        if ligne>0 and ligne<n-1 and cologne>0 and cologne<n-1:
##            if graphe[ligne+1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne] == True:
##                total_cel_V+=1
##            if graphe[ligne][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne+1][cologne-1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne+1] == True:
##                total_cel_V+=1
##            if graphe[ligne-1][cologne-1] == True:
##                total_cel_V+=1
##            if total_cel_V==3:
##                graphe[ligne][cologne]= True
##    #Affichage de la grille
##    for lig in range(n):
##        for col in range(n):
##            print("----",end="")
##        print("-")
##        for col in range(n):
##            if graphe[lig][col]==False:
##                print("| .",end=" ")
##            else:
##                print("| X",end=" ")
##        print("|")
##    for col in range(n):
##            print("----",end="")
##    print("-")
##    print("DEBUG: total_cel_V=",total_cel_V)
##    cologne+=1  
##    if cologne==n:
##        cologne=0
##        ligne+=1
##    cycle-=1
##        
##    #Verification graphe
##    cellules_mortes=0
##    for lig in range(n):
##            for col in range(n):
##                if graphe[lig][col] == False:
##                    cellules_mortes+=1
##    if cellules_mortes==n*n:
##            cel_V=False
