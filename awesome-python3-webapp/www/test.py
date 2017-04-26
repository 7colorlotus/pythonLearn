import orm
from models import User,Blog,Comment
import asyncio
import time

##保存用户信息
async def saveUser(loop):
	await orm.create_pool(loop=loop,user='root',password='root',db='awesome')
	u = User(name='Test',email='test3377@example.com',passwd='12345678',image='about:blank')
	await u.save()
	await orm.destory_pool()
	
#loop = asyncio.get_event_loop()
#loop.run_until_complete(saveUser(loop))


##查找用户信息
async def findUser(loop):
	await orm.create_pool(loop=loop,user='root',password='root',db='awesome')
	u = await User().find('001489397133518833c0fde5a7044fbb7a3d6b3a49209cb000')
	print(u.name)
	await orm.destory_pool()
	
#loop = asyncio.get_event_loop()
#loop.run_until_complete(findUser(loop))


#根据主键删除用户
async def deleteUser(loop):
	await orm.create_pool(loop=loop,user='root',password='root',db='awesome')
	await User(id='001489397133518833c0fde5a7044fbb7a3d6b3a49209cb000').remove()
	print("删除成功")
	await orm.destory_pool()
	
	
#根据主键修改用户	
async def updateUser(loop):
	await orm.create_pool(loop=loop,user='root',password='root',db='awesome')
	await User(id='001489397176476c79dc63d5185423ab9f1865c1699c626000',name='张三',email='zhangsan@qq.com',admin=1,image='about:blank',passwd='12345678',created_at=time.time()).update()
	print("修改成功")
	await orm.destory_pool()	
	
loop = asyncio.get_event_loop()
loop.run_until_complete(updateUser(loop))