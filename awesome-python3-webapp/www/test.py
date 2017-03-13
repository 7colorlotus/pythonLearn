import orm
from models import User,Blog,Comment
import asyncio

'''
async def saveUser(loop):
	await orm.create_pool(loop=loop,user='root',password='root',db='awesome')
	u = User(name='Test',email='test3377@example.com',passwd='12345678',image='about:blank')
	await u.save()
	await orm.destory_pool()
	
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
'''


async def findUser(loop):
	await orm.create_pool(loop=loop,user='root',password='root',db='awesome')
	u = await User().find('001489397133518833c0fde5a7044fbb7a3d6b3a49209cb000')
	print(u.name)
	await orm.destory_pool()
	
loop = asyncio.get_event_loop()
loop.run_until_complete(findUser(loop))