n11,m11=map(int,input().split())
l=[]
k11=[]
sum=1
for i in range(1,n11+1):
	if n11%i==0:
		l.append(i)
for i in range(1,m11+1):
	if m11%i==0:
		k11.append(i)
for i in range(0,len(l)):
	for j in range(0,len(k11)):
		if l[i]==k11[j]:
			sum=sum*l[i]
			
print(sum)
