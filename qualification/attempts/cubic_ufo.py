import math
T=int(input())
for kk in range(T):
	A=float(input())
	delta_phi=math.acos(Decimal(A)*Decimal(math.sqrt(2) )/Decimal(2))  - (math.pi/4)
	a_1=1/2 * math.cos( math.radians(90) + delta_phi)
	a_2=1/2 * math.sin(math.radians(90) + delta_phi)
	a_3=1/2 * math.cos(delta_phi)
	a_4=1/2 * math.sin(delta_phi)
	if (abs(a_1)<0.000000009):
		a_1=0
	if (abs(a_2)<0.000000009):
		a_2=0
	if (abs(a_3)<0.000000009):
		a_3=0
	if (abs(a_4)<0.000000009):
		a_4=0
	print("Case #{}:".format(kk+1))
	print("0 0 0.5")
	print("{} {} 0".format(a_1,a_2))
	print("{} {} 0".format(a_3,a_4))
