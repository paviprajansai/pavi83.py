n11=int(input())
l=list(map(int,input().split()))
for i1 in range(0,len(l)):
	if l[i1+1]!=l[i1]+1:
		print(i1+1)
		break
    #i
