#本质上，decorator就是一个返回函数的高阶函数。

#简单装饰函数
def log(func):
	def wrapper(*args,**kw):
		print("call %s" % func.__name__)
		return func(*args,**kw)
	return wrapper


@log
def now():
	print("2016-08-16 20:41:00")
	
# now()


##################################W
#有参装饰函数
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print("%s %s" % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log("execute")
def now():
	print("2016-08-16 20:41:00")
	
now()
print("now.__name__:",now.__name__)

####################
#使用装饰函数完成aop环绕通知
def log(func):
	def wrapper(*args,**kw):
		print("begin call")
		result = func(*args,**kw)
		print("end call")
		return result
	return wrapper

@log
def f():
	print("calling...")
	return 123


result = f()
print(result)

###############
#引用functools，使用装饰函数完成aop环绕通知


import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print("begin call")
		result = func(*args,**kw)
		print("end call")
		return result
	return wrapper

@log
def f():
    print("calling...")
    return 123
	
result = f()
print(result)
print("f.__name__:", f.__name__)


###############
import functools
def log(text):
	def decorat(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print("begin call")
			print(text)
			result = func(*args,**kw)
			print("end call")
			return result
		return wrapper
	return decorat
@log("execute")
def f():
    print("calling...")
    return 123
	
result = f()
print(result)
print("f.__name__:",f.__name__)

