#定义类
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
		
	def print_score(self):
		print("%s:%s" % (self.name,self.score))
		
	def get_grad(self):
		if self.score > 90:
			return 'A'
		elif self.score > 80:
			return 'B'
		else :
			return 'C'
			
lily = Student('Lily',89)
lucy = Student('Lucy',100)

lily.print_score()
lucy.print_score()

print("Lily's score:",lily.score)

print("Lily's get_grad:",lily.get_grad())
lily.age=10
print("lily.age:",lily.age)

print(lily)

#访问权限
class Student1(object): #object 是指Student1继承object
	def __init__(self,name,score):
		self.__name = name  #定义为私有属性
		self.__score = score
		
	def print_score(self):
		print("%s:%s" % (self.__name,self.__score))
		
	def get_score(self):
		return self.__score
	
	def set_score(self,score):
		self.__score=score
			
lisa = Student1('lisa',89)
lusa = Student1('Lucy',100)

lisa.print_score()
lusa.print_score()

print("lisa's score:",lisa.get_score())
lisa.set_score(100)
print("lisa's score:",lisa.get_score())

lisa.__score=10 #新定义了一个属性，并不是使用类中定义的属性
print("lisa's score:",lisa.get_score())
print("lisa's score:",lisa._Student1__score)#私有变量依然可以访问，但是不能直接访问lisa.__score






