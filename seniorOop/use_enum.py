from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dev'))

#value属性则是自动赋给成员的int常量，默认从1开始计数。
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
	
print("==============================")	
	
#更精确地控制枚举类型，从Enum派生出自定义类
from enum import Enum,unique

@unique #@unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
	Sun=0
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sat=6
	
for name,member in Weekday.__members__.items():
	print(name,'=>',member,',',member.value)
day1 = Weekday(1) #1是枚举值
print("day1:",day1)
print("day1.value:",day1.value)
print("Weekday.Tue:",Weekday.Tue)
print("Weekday['Tue']:",Weekday['Tue'])
print("Weekday['Tue'].value:",Weekday['Tue'].value)
print("day1 == Weekday.Mon:",day1 == Weekday.Mon)
print("day1 == Weekday.Tue",day1 == Weekday.Tue)
Weekday(7)





	
	
