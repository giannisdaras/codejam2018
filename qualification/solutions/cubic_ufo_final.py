import math
from decimal import *
getcontext().prec = 50
T=int(input())
for kk in range(T):
	A=float(input())
	delta_phi=math.acos(Decimal(A)*Decimal(math.sqrt(2) )/Decimal(2))  - (math.pi/4)
	mprosta_x=- Decimal(0.5) * Decimal(math.sin(delta_phi) )
	mprosta_y=Decimal(0.5) * Decimal(math.cos(delta_phi) )
	mprosta_z=0.5

	dexi_x=Decimal(0.5) * Decimal(math.cos(delta_phi))
	dexi_y=Decimal(0.5) * Decimal(math.sin(delta_phi))
	dexi_z=0
	print("Case #{}:".format(kk+1))
	print("0 0 0.5")
	print("{} {} {}".format(dexi_x,dexi_y,dexi_z))
	print("{} {} {}".format(mprosta_x,mprosta_y,mprosta_z))
