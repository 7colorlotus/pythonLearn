def fib(max):
	n,a,b=0,0,1
	while n < max:
		yield b 
		a,b=b,a+b
		n = n + 1
	return "done"
f=fib(8)
while True:
	try:
		x = next(f)
		print("g:",x)
	except StopIteration as e:
		print("Generator return value:",e.value)
		break

		
def triangle(m):
    n, b = 0, [1]
    while n < m:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b) - 1)] + [1]
        n += 1

for x in triangle(10):
    print(x)