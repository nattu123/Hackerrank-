#itertools 
from itertools import permutations 
strng,n = input().split()
n = int(n)
strng= list(strng)
strng.sort()

lst= list(permutations(strng,n))

for i in range(len(lst)):
    for j in range(n):
        print(lst[i][j],end='')
    print('')




 


