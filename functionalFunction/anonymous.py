#关键字lambda表示匿名函数，冒号前面的x表示函数参数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])));


def build(x, y):
	return lambda: x*x + y*y


print("build(3,5):", build(3, 5)())


print((lambda : 11 * 22)())