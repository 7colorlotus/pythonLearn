#hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
#由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
#当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

import asyncio
import threading

@asyncio.coroutine
def hello():
	print('Hello world! (%s)' % threading.currentThread())
	#异步调用asyncio.sleep(1):
	r = yield from asyncio.sleep(1)
	print("Hello again! (%s)" % threading.currentThread())
	
#获取EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
#执行coroutine
#loop.run_until_complete(hello())
loop.run_until_complete(asyncio.wait(tasks))
loop.close()