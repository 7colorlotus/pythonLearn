#python3.5.2使用 easy_install pymysql3 命令安装mysql驱动

import pymysql
import pymysql.cursors

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root',db='mybase',charset='utf8')

cur = conn.cursor()
cur.execute("SELECT * FROM users")
for r in cur:      
      print("row_number:" , (cur.rownumber) )        
      print("name:"+str(r[0])+"  sex:"+str(r[1])+" age:"+str(r[2])) 
cur.close()    
conn.close()