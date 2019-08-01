a11=input()
k11=list(a11)
s11=""
l=""
for i in range(0,len(k11)):
	if i%2==0:
		s11=s11+str(k11[i])+""
	if i%2==1:
		l=l+str(k11[i])+""
print(s11.strip(),end=" ")
print(l.strip())
#i
