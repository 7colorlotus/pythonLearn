import socket

################socket客户端编程###################
#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
#建立连接
s.connect(('www.baidu.com',80))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
#接收数据
buffer = []
while True:
	#每次最多接收1K字节
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#把接收的数据写入文件
with open('baidu.html','wb') as f:
	f.write(html)
s.close




	
	
	
	
	
	
	
	
	
	
	
	
	
	
	