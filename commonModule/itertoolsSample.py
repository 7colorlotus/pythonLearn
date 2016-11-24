import itertools
#迭代数字
natuals = itertools.count(1)
#for n in natuals:
#	print(n)


#cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
#for c in cs:
#	print(c)


#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A',3)
for n in ns:
	print(n)

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
ns = itertools.takewhile(lambda x : x<10,natuals)
print(list(ns))


#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC','XYZ'):
	print(c)
	
	
#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('AAABBBCCCSSSEEAA'):
	print(key,list(group))
	
#groupby()设置忽略大小写
for key,group in itertools.groupby('AAABBBCCCcceEEAA',lambda x:x.upper()):
	print(key,list(group))