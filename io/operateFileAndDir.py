import os

#环境变量
print(os.name) #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
#print(os.uname()) #详细的系统信息，该函数在windows上不提供
print(os.environ) #系统环境变量
print(os.environ.get('PATH')) #获取某个环境变量的值


#操作文件和目录
print(os.path.abspath('.')) #查看当前目录的绝对路径
os.path.join('.','testdir') # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir('./testdir') #然后创建一个目录
os.rmdir('./testdir') #删除一个目录


#拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
os.path.split('./mulLine.txt')
#获取文件的扩展名
os.path.splitext('./mulLine.txt')

#文件重命名
#os.rename('456.jpg','123.jpg')
#os.remove('123.txt')

#复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])