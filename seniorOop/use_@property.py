#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
class Student(object):
	@property   #获取属性值方法
	def score(self):
		return self._score
	
	@score.setter  #设置属性值方法
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError("score must be number!!")
		if value<0 or value>100:
			raise ValueError("score must between 0 and 100")
		self._score=value
		
s = Student()
s.score=100
print("property define score:%s" % s.score)

#s.score=1000 #ValueError: score must between 0 and 100

print("===================================")

class Screen(object):
	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError("width must be a number")
		self._width = value
		
	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError("height must be a number")
		self._height = value
	
	@property
	def resolution(self):	#只读属性
		return "x:%d,y:%d"%(self.width,self.height)
		
screen = Screen()
screen.width=100
screen.height=200

print("screen.resolution: %s",screen.resolution)	


		