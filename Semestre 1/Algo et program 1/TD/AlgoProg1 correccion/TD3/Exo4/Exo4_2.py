'''ROle: Ecrire un programme qui lit une valeur et qui la renverse sans changer son type
Variables: n,i,r: entier
'''

n= int(input("n= "))

#solution fausse
##i= n-1
##while i>=0:
##    r=n-i
##    print(r,end="")
##    i=i-1
##print()
##
##i= 0
##while i<n:
##    r= n-i
##    print(r,end="")
##    i=i+1

#solution 2
##
##for i in range(n-1,-1,-1):
##    r= n-i
##    print(r,end="")
##print()
##for i in range(0,n,1):
##    r= n-i
##    print(r,end="")

#solution vrai

inverse= 0
while n!=0:
    inverse= (inverse*10)+(n%10)
    n= n//10
print(inverse,end="")
