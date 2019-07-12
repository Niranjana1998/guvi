nj1,nj2=map(int,input().split())
for i in range(nj1+1,nj2):
	for j in range(2,i):
		if(i%j==0):
			break
	else:
		print(i,end=" ")
