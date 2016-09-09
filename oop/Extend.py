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

def run_twice(animal):
	animal.run()
	
a = Animal()
a.run()
print("isinstance(a,object)",isinstance(a,object))
b = Cat()
print("isinstance(b,Animal)",isinstance(b,Animal))
b.run()
c = Dog()
c.run()
d=Timer()

run_twice(a)
run_twice(b)
run_twice(c)

#动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
run_twice(d) 

#类属性
class Student(object):
	name='student'
	def __init__(self):
		
	
	
	
	
	
	

