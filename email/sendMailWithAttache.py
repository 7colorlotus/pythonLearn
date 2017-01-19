from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

#定义收发件人	
from_addr = 'zhusheng@ekeyfund.com'
password ='20161107JOBmail'
to_addr='zs_tangming@126.com'
smtp_server = 'smtp.mxhichina.com'

#构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象
msg = MIMEMultipart()

msg['Subject']=Header('好看的画','utf-8').encode()
msg['From']=_format_addr('Python爱好者<%s>' % from_addr)
msg['To']=_format_addr('管理员 <%s>' % to_addr)
content = '<html><body><h1>你好！送一张好看的图片，</h1>' + '<p><img src="cid:0"></p>是不是很好看' + '</body></html>'
msg.attach(MIMEText(content,'html','utf-8'))

with open('C:\\Users\\Administrator\\Desktop\\cat.jpg','rb') as f:
	mime = MIMEBase('image','jpg',filename='cat.jpg')
	mime.add_header('Content-Disposition','attachment',filename='cat.jpg')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')
	#把附件的内容读进来
	mime.set_payload(f.read())
	#用Base64编码
	encoders.encode_base64(mime)
	#添加到MIMEMultipart:
	msg.attach(mime)
	
	
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()	
	
	
	