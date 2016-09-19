#普通创建类
class Hello(object):
	def hello(self,name='world'):
		print("hello,%s"% name)
h = Hello()
h.hello()
print("type(Hello):",type(Hello))
print("type(h):",type(h))


#type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
#我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

#使用type函数创建Hello类。Hello = type('Hello',(object,),dict(hello=fn))
#1.class的名称；
#2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

def fn(name='world'):
	print("hello,%s"% name)

Hello = type('Hello',(object,),dict(hello=fn))
	
h = Hello()
h.hello()
print("type(Hello):",type(Hello))
print("type(h):",type(h))


#除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass是类的模板，所以必须从`type`类型派生
class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
	pass
l = MyList()
l.add("123")
print("l:",l)


#ORM(Object Relational Mapping)使用metaclass的样例

class Field(object):
	def __init__(self,name,colum_type):
		self.name=name
		self.colum_type=colum_type
	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__,self.name)

class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,'bigint')

class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name=='Model':
			return type.__new__(cls,name,bases,attrs)
		print('Found model:%s' % name)
		mappings = dict()
		for k,v in attrs.items():
			if isinstance(v,Field):
				print('Found mapping:%s ==> %s' % (k,v))
				mappings[k]=v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__']=mappings # 保存属性和列的映射关系
		attrs['__table__']=name # 假设表名和类名一致
		return type.__new__(cls,name,bases,attrs)
		
class Model(dict,metaclass=ModelMetaclass):
	def __init__(self,**kw):
		super(Model,self).__init__(**kw)
	
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
	
	def __setattr__(self,key,value):
		self[key]=value
		
	def save(self):
		fields = []
		params = []
		args = []
		for k,v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self,k,None))
		sql = 'insert into %s (%s) values(%s)' %(self.__table__,','.join(fields),','.join(params))
		print('SQL:%s' % sql)
		print('ARGS:%s' % str(args))
		
class User(Model):
	id=IntegerField('id')
	name=StringField('username')
	email=StringField('email')
	passwd=StringField('password')
	
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()









