#i
a1,d1,n1=map(int,input().split())
s1=0
for i in range(1,n1+1):
	s1=s1+a1+(i-1)*d1
print(s1)
