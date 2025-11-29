def tri_ins(tab: list[int], dim: int) -> list[int]:
    for i in range(1,dim):
        if tab[i] < tab[i-1]:
            tmp = tab[i]
            tab[i] = tab[i-1]
            tab[i-1] = tmp
        j=i
        while j>0:
            if tab[j] < tab[j-1]:
                tmp = tab[j]
                tab[j] = tab[j-1]
                tab[j-1] = tmp
            j-=1

import random
dim= 10
t= [random.randint(0,20) for i in range(dim)]
print(t)
tri_ins(t,dim)  
print(t)