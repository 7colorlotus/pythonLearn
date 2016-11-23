import re

#常用正在表达式
mail = 'zs_tangming@126.com';
result = re.match(r'\w+@{1}\w+.{1}\w+',mail)
if result:
	print('ok')
else:
	print('fail')
	
str = 'a b c  d     e'
strList = re.split(r'\s+',str)
print(strList)

#使用正则表达式切分字符串
str = 'a,b,c  d     e'
strList = re.split(r'[\s,]+',str)
print(strList)

str = 'a,b,;c ; d     e'
strList = re.split(r'[\s,;]+',str)
print(strList)


#正则表达式分组 
#正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})','010-123562')
print("m.group(0):",m.group(0))
print("m.group(1):",m.group(1))
print("m.group(2):",m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
re.match(r'^(\d+)(0*)$', '102300').groups()
#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
#必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
re.match(r'^(\d+?)(0*)$', '102300').groups()

#编译

#当我们在Python中使用正则表达式时，re模块内部会干两件事情：
#1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
#2.用编译后的正则表达式去匹配字符串。
#如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

print(re_telephone.match('010-123652').groups())
print(re_telephone.match('010-856652').groups())



re_email = re.compile(r'[a-zA-Z.]+@\w+.\w')
if re_email.match('someone@gmail.com'):
	print('ok')
	
if re_email.match('bill.gates@microsoft.com'):
	print('ok')
	
 	
if re.match(r'<\w+\s\w+>\s[a-zA-Z.]+@\w+.\w','<Tom Paris> tom@voyager.org'):
	print('ok')
else:
	print('fail')

























