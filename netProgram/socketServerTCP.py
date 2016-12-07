################socket服务端编程###################
import socket
import time,threading


def tcplink(sock,addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5) #调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
print('Waiting for connetion...')
while True:
	#接受一个新连接
	sock,addr = s.accept()
	#创建新线程来处理TCP连接
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()

	

	