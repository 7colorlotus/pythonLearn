#自定义打印对象
class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object(name:%s)' %self.name
	
	def __getattr__(self,attr):
		if attr == 'score': #当没有score属性时，返回指定的值
			return 99
		if attr == 'age':
			return lambda :25
			
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
	#def __call__(self):
	#	print('My name is %s.' % self.name)
		

print(Student("Lily"))
#print(Student("Lily")()) #需要在类中定义__call__(self)方法
print(Student("Lily").score)
print(Student("Lily").age())
print(callable(Student))
print(callable(Student("Lily")))
#print(Student("Lily").abc)

#自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
print("===========================")
class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1
	def __iter__(self):
		return self   # 实例本身就是迭代对象，故返回自己
	def __next__(self):
		self.a,self.b = self.b,self.a+self.b # 计算下一个值
		if self.a > 100000: # 退出循环的条件
			raise StopIteration()
		return self.a # 返回下一个值
	def __getitem__(self,n):
		a,b=1,1
		if isinstance(n,int):
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop  = n.stop
			if start is None:
				start=0
			a,b=1,1
			L=[]
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b=b,a+b
			return L
		
print(Fib()[0])	

print(Fib()[0:5])	
#for n in Fib():
#	print(n)


#链式调用，打印rest地址
print("===========链式调用================")
class Chain(object):
	def __init__(self,path=''):
		self.path=path
	def __getattr__(self,path):
		return Chain('%s/%s' % (self.path,path))
	def __str__(self):
		return self.path
	__repr__=__str__
	
print(Chain().status.user.timeline.list)
	
	
	
	