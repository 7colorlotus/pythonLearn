from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib

#解码方法
def decode_str(s):
	value,charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
	return value
	
#检测编码
def guess_charset(msg):
	charset = msg.get_charset()
	if charset is None:
		content_type = msg.get('Content-Type','').lower()
		pos = content_type.find('charset=')
		if pos >= 0:
			charset = content_type[pos+8:].strip()
	return charset

#输出邮件信息
def print_info(msg,indent=0):
	if indent == 0:
		for header in ['From','To','Subject']:
			value = msg.get(header,'')
			if value:
				if header=='Subject':
					value = decode_str(value)
				else:
					hdr,addr = parseaddr(value)
					name = decode_str(hdr)
					value = u'%s <%s>' % (name,addr)
			print('%s%s: %s' % (' ' * indent,header,value))
	if(msg.is_multipart()):
		parts = msg.get_payload()
		for n,part in enumerate(parts):
			print('%spart %s' % (' ' * indent,n))
			print('%s--------------' % (' ' * indent))
			print_info(part,indent + 1)
	else:
		content_type = msg.get_content_type()
		if content_type=='text/plain' or content_type=='text/html':
			content = msg.get_payload(decode=True)
			charset = guess_charset(msg)
			if charset:
				content = content.decode(charset)
			print('%sTest: %s' % (' ' * indent,content+'...'))
		else:
			print('%sAttachment:%s' % (' ' * indent,content_type))
	



email='zhusheng@ekeyfund.com'
password='20161107JOBmail'
pop3_server='pop3.mxhichina.com'


#连接到pop3服务器
server = poplib.POP3(pop3_server)
#可以打开或关闭调试信息
server.set_debuglevel(1)
#可选：打印POP3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))


#身份认证：
server.user(email)
server.pass_(password);

print('Messages: %s. Size:%s' % server.stat())
#list()返回所有邮件的编号
resp,mails,octets = server.list()
#可以查看返回的列表类似
print(mails)

#获取最新一封邮件，注意索引号从1开始:
index = len(mails)
resp,lines,octets = server.retr(index)

#lines存储了邮件的原始文本的每一行
#可以获得整个邮件的原始文本：
msg_content = b'\r\n'.join(lines).decode('utf-8')
#稍后解析出邮件:
msg = Parser().parsestr(msg_content)

print_info(msg)

#可以根据邮件索引号直接从服务器删除邮件
#server.dele(index)
#关闭连接：
server.quit()


















