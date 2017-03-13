import orm
from models import User,Blog,Comment


def test():
	yield from orm.create_pool(user='root',password='root',db='awesome')
	u = User(name='Test',email='test2@example.com',passwd='12345678',image='about:blank')
	yield from u.save()
	
for x in test():
	pass