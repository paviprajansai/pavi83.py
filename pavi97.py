n11=int(input())
s11=0
while n11>0:
	r11=n11%10
	s11=(s11*10)+r
	n11=n11//10
print(s11)
