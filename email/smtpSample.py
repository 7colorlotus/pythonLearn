from email.mime.text import MIMEText
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
to_addr='626477293@qq.com'
smtp_server = 'smtp.mxhichina.com'

#封装消息
msg = MIMEText('hello,send by Python...','plain','utf-8')

#若想发送html邮件，只需修改'plain'为html即可
#msg = MIMEText('<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', 'html', 'utf-8')

msg['Subject']=Header('来自SMTP的问候......','utf-8').encode()
msg['From']=_format_addr('Python爱好者<%s>' % from_addr)
msg['To']=_format_addr('管理员 <%s>' % to_addr)


server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()