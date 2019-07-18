#偏函数 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

result = int('12253',base=8)
print(result)

import functools
int16 = functools.partial(int,base=16)
print(int16('12253'))