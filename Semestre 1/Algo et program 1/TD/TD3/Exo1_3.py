'''ROle: Ecirre un program qui lit factoriel positif et qui calcul et affiche
le nombre total
Variables: n,j,i
'''

#On procede a la lecture

n= int(input("Donnez moi n= "))
while n== 0:
    print("Le nombre ne peut pas etre egal a 0")
    n= int(input("Donnez moi n= "))

i= 1
j= n
while i< n:
    j= j* (i)
    i= i+1
print(j)

##n= int(input("Donnez moi n= "))
##while n== 0:
##    print("Le nombre ne peut pas etre egal a 0")
##    n= int(input("Donnez moi n= "))
##j= n
##for i in range(1,n,1):
##    j= j*i
##print(j)
##

####solution 2
##
##i= 1
##j= 1
##while i<= n:
##    j= j* (i)
##    i= i+1
##print(j)
##
####solution 3
##
##i= n
##j= 1
##while i>=1:
##    j= j* (i)
##    i= i-1
##print(j)




