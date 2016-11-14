#python调试的集中方式
#1.print直接打印
#2.assert 断言处理
#3.log 日志处理
#4.pdb 逐行调试

def fooPrint(s):
	n = int(s)
	print(">>>n=%d" % s)
	print(10/n)
	
def fooAssert(s):
	n = int(s)
	assert n !=0 ,'n is zero!' #如果不为0，则正常执行；如果为0，则抛出AssertionError异常，异常信息为"n is zero!"

import logging
logging.basicConfig(level=logging.INFO)#默认是debug级别
def fooLog(s):
	n = int(s)
	logging.info(">>>n=%d" % s)
	print(10/n)
	
#使用命令python3 -m pdb debugModel.py执行调试
	#1.输入命令l来查看代码
	#2.输入命令n可以单步执行代码
	#3.任何时候都可以输入命令p 变量名来查看变量
	#4.输入命令q结束调试，退出程序
def fooPdb(s):
	n = int(s)
	print(10/n)
	
fooPdb(2)

import pdb

#在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
def fooPdbMethod(s):
	n = int(s)
	pdb.set_trace() # 运行到这里会自动暂停,c继续运行到下一个断点或者执行结束
	print(10/n)
	
fooPdbMethod(5)