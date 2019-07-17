nj1,nj2=map(int,input().split())
nj=[]
for z in range(nj1,nj2+1):
    for p in range(2,z):
        if(z%p==0):
            break
    else:
        nj.append(z)
print(len(nj))
