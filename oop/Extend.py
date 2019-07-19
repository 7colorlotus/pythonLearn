#继承
class Animal(object):
	def run(self):
		print("Animal is running....")


class Cat(Animal):
	def run(self):
		print("Cat is running....")


class Dog(Animal):
	def run(self):
		print("Dog is running....")


class Timer(object):
	def run(self):
		print("Timer is running....")


class Tortoise(Animal):
		def run(self):
			print("Tortoise is running slowly....")


def run_twice(animal):
	animal.run()
	animal.run()


if __name__ == '__main__':
	a = Animal()
	a.run()
	print("isinstance(a,object)",isinstance(a, object))
	b = Cat()
	print("isinstance(b,Animal)",isinstance(b, Animal))
	b.run()
	c = Dog()
	c.run()
	d=Timer()

	run_twice(a)
	run_twice(b)
	run_twice(c)

	#动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
	#这里只要d对象有run方法就可以传入参数
	run_twice(d)

	run_twice(Tortoise())

		
	
	
	
	
	
	

