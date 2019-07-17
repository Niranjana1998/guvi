nj1=int(input())
nj2=[]
for i in range(nj1):
  c=input()
  nj2.append(c)
d=[]
for i in zip(*nj2):
  if(i.count(i[0])==len(i)):
    d.append(i[0])
  else:
    break
print(''.join(d))
