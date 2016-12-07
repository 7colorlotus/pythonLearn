import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #SOCK_DGRAM指定UDP
s.bind(('127.0.0.1',9991)) #绑定端口
print('Bind UDP on 9991') 
#不需要调用listen()方法，而是直接接收来自任何客户端的数据
while True:
	data,addr = s.recvfrom(1024)
	print('Received from %s:%s.' % addr)
	s.sendto(b'Hello, %s' % data,addr)
