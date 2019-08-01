n1=int(input())
l=list(map(int,input().split()))
m1=0
a1=[]
for i1 in range(n1-1):
    if l[i1]>l[i1+1]:
        a.append(l[i1])
    else:
        a1.append(l[i1+1])
print(sum(a1))
