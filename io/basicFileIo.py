#普通读取文件的方法

try:
	f = open('ioSampleDoc.txt','r')
	print(f.read())
finally:
	if f:
		f.close()
		

#使用with,自动帮我们调用close()方法

with open('ioSampleDoc.txt','r') as f:
	print(f.read())
	
#read(size)最多读取size个字节的内容,readline()读取一行
with open('mulLine.txt','r') as f:
	for line in f.readlines():
		print(line.strip())
		
#file-like Object
#像open()函数返回的这种有个read()方法的对象，
#在Python中统称为file-like Object。
#除了file外，还可以是内存的字节流，网络流，自定义流等等。
#file-like Object不要求从特定类继承，只要写个read()方法就行。
#StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

#读取二进制文件
#with open('123.jpg','rb') as f:
	#print(f.read())
	
with open('中文.txt','r',encoding='GBK') as f:
	print(f.read())
	
	
#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
from datetime import datetime
with open('写文件.txt','w',encoding='UTF-8') as f:
	f.write('今天是')
	f.write(datetime.now().strftime('%Y-%m-%d'))