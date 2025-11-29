#Role: Comparer une valeur en C et une valeur en F
#Variables:
#C entier
#F entier

C= int(input("DOnne moi la temperature en C\n"))
F= (9/5)*C+32

if C == F:
     print("La temperature en Celsius est la meme qu'en Farenheit cad", C)
   
elif C > F:
    print("La temperature", C,"en celsius es plus grande que celle en", F,"Farenheit")

else:
    print("La temperature", C,"en celsius est plus petite que celle en", F,"Farenheit")
