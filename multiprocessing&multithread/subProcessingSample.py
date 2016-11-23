#下面代码相当于在命令行执行命令nslookup
import subprocess
print("$ nslookup")
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\nbaidu.com\nexit\n')
print(output.decode('gbk')) #cmd默认gbk,在xnix上使用utf-8解码
print('Exit code:',p.returncode)