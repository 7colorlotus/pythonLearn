from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类：
Base = declarative_base()

class User(Base):
	__tablename__='user'
	
	id=Column(String(20),primary_key=True)
	name=Column(String(20))
	
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/mybase')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user=User(id='5',name='ttttttt')
session.add(new_user)
session.commit()
session.close()