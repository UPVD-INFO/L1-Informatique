n= int(input("n= "))

if n==0 or n==1:
    fibo_n=n
for i in range(2,n+1):
    fibo_n=fibo_nm1+fibo_nm2
    fibo_nm2=fibo_nm1
    fibo_nm1= fibo_n

print(fibo_n)

