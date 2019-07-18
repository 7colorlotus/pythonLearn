#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：

def is_palindrome(n):
	return n==int(str(n)[::-1])

print(list(filter(is_palindrome,range(1,1000))))



print("abcdefg"[::-1])

def is_boy(student):
	return 'boy' == student.split("_")[1]


print(list(filter(is_boy,{"zhangsan_boy","lisi_boy","wangwu_girl"})))

