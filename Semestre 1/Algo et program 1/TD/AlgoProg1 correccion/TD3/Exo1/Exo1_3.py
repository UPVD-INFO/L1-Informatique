'''ROle: Ecirre un program qui lit factoriel positif et qui calcul et affiche
le nombre total
Variables: n,j,i
'''

#On procede a la lecture

n= int(input("Donnez moi n= "))

##if n== 0:
##    f= 1
##else:
##    i= 1
##    f= 1
##    while i<= n:
##        f= f* (i)
##        print(i,f)
##        i= i+1
##print(f)

##n= int(input("Donnez moi n= "))
##if n== 0:
##    f=1
##else:
##    f= 1
##    for i in range(1,n+1,1):
##        f= f*i
##print(f)


####solution 2
if n==0:
    f=1
else:
    f=1
    for i in range(n,0,-1):
        f= f*i
print(f,end='')

####solution 3
##
##i= n
##j= 1
##while i>=1:
##    f= f* (i)
##    i= i-1
##print(f)




