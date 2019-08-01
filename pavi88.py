def gcd(n1,m1):
  if m1==0:
    return(n1)
  else:
    return(gcd(m1,n1%m))
n1,m1=map(int,input().split())
p1=gcd(n1,m1)
l=(n1*m1)//p1
print(l)
