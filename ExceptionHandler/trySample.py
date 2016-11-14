#Python所有的错误都是从BaseException类派生的
print("sample1--------------------------------")
try:
	print('try...')
	r = 10 / 0
	print("result:",r)
except ZeroDivisionError as e:
	print("excpetion:",e)
finally:
	print('finally...')
print('END')

print("sample2--------------------------------")
try:
	print('try...')
	r = 10/int('a')
	print("result:",r)
except ValueError as e:
	print("ValueError:",e)
except ZeroDivisionError as e:
	print("ZeroDivisionError:",e)
finally:
	print("finally...")
print("END")


print("sample3--------------------------------")
def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s)/2
	
def main():
	try:
		print("result:",bar('1'))
	except Exception as e:
		print('Error:',e)
	finally:
		print('finally...')
		
main()

