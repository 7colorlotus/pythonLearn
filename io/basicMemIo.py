from io import StringIO
strIo = StringIO('123')

#strIo.tell查看当前游标位置，strIo.seek设置游标位置
if strIo.tell != len('123'):
	strIo.seek(len('123'))
	
print("strIo.write('Hello'):",strIo.write('Hello'))
print("strIo.write(' '):",strIo.write(' '))
print("strIo.write('World!!'):",strIo.write('World!!'))
print("strIo.getvalue():",strIo.getvalue())


strIo = StringIO('Hello!\nHi\nGoodbye!\n')
while True:
	str = strIo.readline()
	if str == '':
		break
	print(str.strip())
	
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO
byteIo = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87');
print(byteIo.read())