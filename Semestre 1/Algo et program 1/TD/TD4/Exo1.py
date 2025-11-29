n= int(input("n= "))

for i in range(n):
    for j in range(1,n+1-i):
        print(j,end="")
    for j in range(i):
        print(" ",end="")
    for j in range(i-1):
        print(" ",end="")
    for j in range(n-i,0,-1):
        if j!=n:
            print(j,end="")
    print()
for i in range(n-1):
    for j in range(1,n+i):
        print(j,end="")
    for j in range(2*i-1):
        print(" ",end="")
##    for j in range(i):
##        print(" ",end="")
    for j in range(n-1,0,-1):
        print(j,end="")
    print()
print()
for i in range(0,n,1):
	for j in range(1,n+1-i,1):
		print(j,end='')
	for j in range(2*i-1):
		print(' ',end='')
	for j in range(n-i,0,-1):
		if  j !=n:
			print(j,end='')
	print()
for i in range(n-2,-1,-1):
    print(j,end='')
    for j in range(2*i-1):
        print(' ',end='')
    for j in range(n-i,0,-1):
        if  j !=n:
            print(j,end='')
    print()
print()

# ... partie supperieure du carree
for i in range(0, n):
  # ... pour chaque ligne i, afficher les elements 1 ... n-i+1
  for j in range(1, n-i+1):
    print(j, end='')
  # ... afficher ensuite i espace
  for j in range(2*i-1):
    print(' ', end='')
  # ... et finalement, afficher les elements n-i ... 1
  for j in range(n-i, 0, -1):
    # /!\ si j == n, donc i == 0, on n'affiche pas j
    if j != n:
      print(j, end='')
  print()
# ... de maniere identique, partie inferieur, en inversant le sens de la boucle
#     sur i
for i in range(n-2, -1, -1):
  for j in range(1, n-i+1):
    print(j, end='')
  for j in range(2*i-1):
    print(' ', end='')
  for j in range(n-i, 0, -1):
    if j != n:
      print(j, end='')
  print()
