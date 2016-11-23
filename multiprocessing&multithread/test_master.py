from multiprocessing.managers import BaseManager
from multiprocessing import Process, Queue,freeze_support

queue = Queue()

def return_queue():
	global queue
	return queue


class QueueManager(BaseManager): pass

def test():
	QueueManager.register('get_queue', callable=return_queue)
	m = QueueManager(address=('127.0.0.1', 50000), authkey=b'abracadabra')
	#s = m.get_server()
	#s.serve_forever()
	m.start()


if __name__=='__main__':
	freeze_support()
	test()