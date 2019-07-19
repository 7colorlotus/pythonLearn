# python中的类
# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，
# 但拥有的变量名称都可能不同


# 定义类
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
		
	def print_score(self):
		print("%s:%s" % (self.name, self.score))
		
	def get_grad(self):
		if self.score > 90:
			return 'A'
		elif self.score > 80:
			return 'B'
		else:
			return 'C'


# 访问权限
# object 是指Student1继承object
class Student1(object):
	def __init__(self, name, score):
		# 定义为私有属性__
		self.__name = name
		self.__score = score
		
	def print_score(self):
		print("%s:%s" % (self.__name, self.__score))
		
	def get_score(self):
		return self.__score
	
	def set_score(self, score):
		self.__score = score


if __name__ == '__main__':
	lily = Student('Lily', 89)
	lucy = Student('Lucy', 100)

	lily.print_score()
	lucy.print_score()

	print("Lily's score:", lily.score)

	print("Lily's get_grad:", lily.get_grad())
	lily.age = 10
	print("lily.age:", lily.age)

	print(lily)
	print("==========================================")

	lisa = Student1('lisa', 89)
	lusa = Student1('Lucy', 100)

	lisa.print_score()
	lusa.print_score()

	print("lisa's score:", lisa.get_score())
	lisa.set_score(100)
	print("lisa's score:", lisa.get_score())

	# 新定义了一个属性，并不是使用类中定义的属性
	lisa.__score=10
	print("lisa's score:", lisa.get_score())
	# 私有变量依然可以访问，但是不能直接访问lisa.__score
	print("lisa's score:", lisa._Student1__score)


