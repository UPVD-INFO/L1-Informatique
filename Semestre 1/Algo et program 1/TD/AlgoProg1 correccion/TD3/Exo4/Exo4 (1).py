'''Role: Ecrire un programme qui inverse les valeurs
Variables: n,,r: entier
'''

n= int(input("Donne moi n= "))
####solution fausse#####
###solution 1
##i= 1
##inverse= []
##while i<=n:
##    inverse.append(i)
##    i= i+1
##print(inverse ,"avant")
##inverse.reverse()
##print(inverse,"apres")
##
###solution 2
##inverse= []
##for i in range(1,n+1,1):
##    inverse.append(i)
##print(inverse, "avant")
##inverse.reverse()
##print(inverse, "apres")

######solution vrai######


##r=0
##while n>0:
##   r= n%10
##   print(r,end="")
##   n= n//10
##   if n>0:
##       print(",",end="")
##print(".",end="")

r=0
for i in range(1,n,n*10):
   r= n%10
   print(r,end="")
   n= n//10
   if n>0:
       print(",",end="")
print(".",end="")
