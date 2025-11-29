n= int(input("n= "))

##i=1
##s=0
##while i<n:
##    if (n%i)==0:
##        s= s+i
##    i= i+1

s=0
for i in range(1,n,1):
    if (n%i) == 0:
        s= s+i

if s == n:
    print(s,"est un nombre parfait")
else:
    print(s,"n'est pas un nombre parfait")
