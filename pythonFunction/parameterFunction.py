

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

#默认参数
#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

def power(x,n=2):
	sum=x
	while(n>0):
		n = n -1
		sum = sum * x
	return sum	
#print(power(3,5))

#list问题

def add_end(L=None):
    if L is None:
	    L=[]
    L.append('END')
    return L
	
#print(add_end())
#print(add_end())


#可变参数
def cal(*numbers):
	sum=0
	for n in numbers:
		sum=sum + n*n
	return sum 
	
#print(cal(3,4,5,6))
#print(cal())

#关键字参数
def person(name,age,**kw):
	print("name:",name,"age:",age,"other:",kw)

#person("zhangsan",19)
#other={"job":"engineer","city":"shanghai"}
#person("zhangsan",19,city=other['city'],job=other['job'])
#person("zhangsan",19,**other)

#命名关键字参数 
def person2(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print("name:",name,"age:",age,"other:",kw)
	
#other={"job":"engineer","city":"shanghai"}	
#person2("zhangsan",19,city=other['city'],job=other['job'])


def person3(name,age,*,city,job):
	print(name,age,city,job)
person3("lotus",28,city="上海",job="engineer")
	
