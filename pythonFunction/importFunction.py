import math


def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny


print(move(10, 20, 100))
print(math.sin(0))