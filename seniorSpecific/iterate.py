#Iterable迭代

#只要isinstance为True的都可以使用迭代
from collections import Iterable

print("isinstance(\"123\",Iterable)：",isinstance("123",Iterable))
print("isinstance(123,Iterable)：",isinstance(123,Iterable))
print("isinstance([1,3,4,5],Iterable)：",isinstance([1,3,4,5],Iterable))
print("isinstance({'A':3,'B':4,'C':5},Iterable):",isinstance({'A':3,'B':4,'C':5},Iterable))


d = {'A':3,'B':4,'C':5}
for key in d:
	print(key)

for value in d.values() :
	print(value)
	
for k,v in d.items() :
	print("k=",k,",v=",v)
	
L=[1,3,4,5]
for i,value in enumerate(L) :
	print("i=",i,",value=",value)