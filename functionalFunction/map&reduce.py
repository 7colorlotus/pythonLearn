#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：


def normalize(name):
    result = ''
    for i,value in enumerate(name):
        if i==0:
            result+=value.upper()
        else:
            result+=value.lower()
    return result
	
print(list(map(normalize,['adam', 'LISA', 'barT'])))



#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

from functools import reduce
def prod(L):
	def mul(x,y):
		return x*y
	return reduce(mul,L)
	
print(prod([1,3,4,5,6]))


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
	index = s.find('.')+1
	length = len(s[index:])
	newS = s.replace('.','')
	def char2num(c):
		return  {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
	
	def fn(x,y):
		return x*10 + y
	result = reduce(fn,map(char2num,newS))
	print(pow(10,length))
	result = result / pow(10,length)
	return result
print(str2float("123.5633433"))


def last_name(name):
	if(isinstance (name, str)):
		return name.split(" ")[1];
	else:
		return 0

print(list(map(last_name, ["zhang san","li si","wang wu", 123])))