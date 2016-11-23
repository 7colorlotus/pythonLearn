#namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
print("========namedtuple================")
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x)
print(p.y)


print(isinstance(p,Point))
print(isinstance(p,tuple))


#deque
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

print("========deque================")
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
print("========defaultdict================")
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1']=123
print(dd['key1'])
print(dd['key2'])

#OrderedDict 有序的dict
print("========OrderedDict================")
from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
print(d)
od=OrderedDict([('a',1),('b',2),('c',3)])
print(od)

#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self,capacity):
		super(LastUpdatedOrderedDict,self).__init__() #同super().__init__()
		self._capacity=capacity
	
	def __setitem__(self,key,value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False) # last=false时按FIFO顺序返回
			print("remove:",last)
		if containsKey:
			del self[key]
			print('set:',(key,value))
		else:
			print('add:',(key,value))
		OrderedDict.__setitem__(self,key,value) # 调用父类的__setitem__方法写入键值对
	
luod = LastUpdatedOrderedDict(2);
luod['key1']=123
luod['key2']=456
luod['key3']=789
print(luod)


#Counter
#Counter是一个简单的计数器
print("========Counter================")
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)



























