#简单序列化与反序列化
import pickle
d = dict(name='bob',age=20,score=80)
print(pickle.dumps(d))
with open("dump.txt","wb") as f:
	f.write(pickle.dumps(d))
with open("dump.txt","rb") as f:
	d = pickle.load(f)
	print(d)
	
#JSON与python
#JSON类型   Python类型
#{}	        dict
#[]	        list
#"string"	str
#1234.56	int或float
#true/false	True/False
#null	    None

#Json序列化类对象
import json
d=dict(name='bob',age=20,score=80)
dJson = json.dumps(d)
print("dJson==>",dJson)
d2 = json.loads(dJson)
print("d2==>",d2)

class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score

s = Student('zs',19,80)
print(json.dumps(s,default=lambda obj:obj.__dict__))