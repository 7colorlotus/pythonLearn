#解方程ax2 + bx + c = 0
import math
def fc(a,b,c):
	if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(b,(int,float))
		raise TypeError('bad oprand type')
	x1 = (-b + math.sqrt(b*b - 4*a*c))/2*a
	x2 = (-b - math.sqrt(b*b - 4*a*c))/2*a
	return x1,x2
		