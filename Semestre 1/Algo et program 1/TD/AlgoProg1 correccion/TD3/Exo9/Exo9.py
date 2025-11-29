r= int(input("Entrer le rayon= "))

for l in range(2*r+1):
    for c in range(2*r+1):
        if (r-c)*(r-c)+(r-l)*(r-l)<= (r)*(r):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for l in range(2*r+1):
    for c in range(2*r+1):
        if (r-c)*(r-c)+(r-l)*(r-l)>r*r and (r-c)*(r-c)+(r-l)*(r-l)<=(r+1)*(r+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
