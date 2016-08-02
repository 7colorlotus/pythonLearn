d={"zhangsan":18,"lisi":22,"wangwu":33}
print('d:%s' % d)
print('zhangsan age is %s' % d['zhangsan'])
print('zhangsan in d : %s' % ('zhangsan' in d))
print('pop zhangsan:%s' % d.pop('zhangsan'))
print('d:%s' % d)
print('d.get zhangsan %s' % d.get('zhangsan','no'))