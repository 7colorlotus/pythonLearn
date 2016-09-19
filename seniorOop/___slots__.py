class Student(object):
	pass

s = Student()
s.name='Lucy'
s.age=18
s.score=99


print("s's name :%s,age:%s,score:%s" %(s.name,s.age,s.score))
print("========================================")

#为对象动态添加方法
def set_age(self,age):
	self.age=age
	
from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print("s get age from add method,age:%s" % s.age)
print("========================================")

#给对象添加的属性或方法，不会应用到该类的其他实例上
s2 = Student();
#print("s2's name :%s,age:%s,score:%s" %(s2.name,s2.age,s2.score)) #AttributeError: 'Student' object has no attribute

#为类动态添加方法
def set_score(self,score):
	self.score=score

Student.set_score=set_score
s.set_score(100)
print("s's name :%s,age:%s,score:%s" %(s.name,s.age,s.score))
print("========================================")

#使用__slots__
class Student2(object):
	__slots__=('name','age') # 用tuple定义允许绑定的属性名称

s3 = Student2()
s3.name='zs'
s3.age=18
s3.score=99   #AttributeError: 'Student2' object has no attribute 'score'

#总结__slots__只能应用到当前类，子类或父类不受影响。若子类父类需要受到约束，在其类内部定义__slots__























