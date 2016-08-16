#返回函数
#1.一个函数可以返回一个计算结果，也可以返回一个函数。
#2.返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

def lazySum(*args):
	def sum():
		result=0
		for n in args:
			result=result + n
		return result
	return sum

f=lazySum(1,33,4,5,5,2)
f1=lazySum(1,33,4,5,5,2)
print("f:",f)
print("f==f1:",f==f1)
print("f():",f())


def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f);
	return fs
	
f1,f2,f3=count()
print("f1():",f1())
print("f2():",f2())
print("f3():",f3())


def count2():
	fs=[]
	def f(j):
		def g():
			return j*j
		return g
	
	for i in range(1,4):
		fs.append(f(i));
	return fs
	
f1,f2,f3=count2()
print("f1():",f1())
print("f2():",f2())
print("f3():",f3())

