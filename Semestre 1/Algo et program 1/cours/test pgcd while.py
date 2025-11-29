a= int(input("a= "))
b= int(input("b= "))

if a < b:
	tmp = a
	a = b
	b = tmp
	c = a-b
	while c!= 0 :
		a = c
		if a < b:
			tmp = a
			a = b
			b = tmp
		c = a-b
p = a
print( "pgcd= ",p)
