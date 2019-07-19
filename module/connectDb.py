# 使用mysql模块处理mysql数据库

import pymysql.cursors

# 连接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='python_db',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 插入一条记录
        sql = "INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster', '15'))

    # 连接不是自动提交的，需要手动提交
    connection.commit()

    with connection.cursor() as cursor:
        # 读取一条记录
        sql = "SELECT `id`, `age` FROM `users` WHERE `name`=%s"
        cursor.execute(sql, ('webmaster'))
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()