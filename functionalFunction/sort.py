#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
def by_name(t):
	def getName(tt):
		return tt[0]
	return list(sorted(t,key=getName))
	
print("by_name:",by_name([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]))


#再按成绩从高到低排序：

def by_score(t):
	def getScore(tt):
		return tt[1]
	return list(sorted(t,key=getScore,reverse=True))
	
print("by_score:",by_score([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]))