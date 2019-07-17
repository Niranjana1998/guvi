from itertools import permutations
nj1=input()
nj2=permutations(nj1)
for i in list(nj2):
    print("".join(i))
