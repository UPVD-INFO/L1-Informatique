#Variables: d,r,h,m,s entier

d= int(input("Quelle est la durée"))

h= d//3600
r= d%3600
m=r//60
s= r % 60

print(f"{h}:{m}:{s}")
