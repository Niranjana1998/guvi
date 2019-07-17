n=int(input())
l=list(map(int,input().split()))
nj1=l[:n//2]
nj2=l[n//2:]
if(sum(nj1)//len(nj1)==sum(nj2)//len(nj2)):
	print('yes')
	exit()
print('no')
