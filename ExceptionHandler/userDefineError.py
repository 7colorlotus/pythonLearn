#自定义异常,继承已有的异常

class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if(n==0):
		raise FooError("invalide value:%s"% s)
	return 10/n

foo('2')


#raise语句如果不带参数，就会把当前错误原样抛出
def bar():
	try:
		10/0
	except ValueError as e:
		print("ValueError e:",e)
		raise 

bar()