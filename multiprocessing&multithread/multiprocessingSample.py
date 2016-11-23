#import os
#print('Process (%s) start...' %os.getpid())
 #Only works on Unix/Linux/Mac:
#pid = os.fork()
#if pid == 0:
#	print("I am child process (%s) and my parnet is %s." %(os.getpid(),os.getppid()))
#else:
#	print('I (%s) just created a child process (%s).' %(os.getpid,pid))

#常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。


#multiprocessing模块提供了一个Process类来代表一个进程对象
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s)...' %(name,os.getpid()))

if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc,args=('test',)) #创建子进程时，只需要传入一个执行函数和函数的参数
	print('Child process will start.')
	p.start() #创建一个Process实例，用start()方法启动
	p.join()  #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	print('Child process end')
	

#进程池
print("================pool===================")
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print('Run task %s (%s)...' %(name,os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Tasks %s runs %0.2f sconds.' %(name,(end-start)))
	
if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('Waiting for all subprocesses done...')
	p.close() #调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
	p.join()  #对Pool对象调用join()方法会等待所有子进程执行完毕
	print('All subprocesses done.')
    #task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。
	#由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
	

#子进程 
print("==============subprocess=====================")
import subprocess
r=subprocess.call(['nslookup','www.baidu.com'])
print('Exit code:',r)



#进程间通信
#Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。









































