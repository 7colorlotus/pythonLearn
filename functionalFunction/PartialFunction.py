result = int('12253',base=8)
print(result)

import functools
int16 = functools.partial(int,base=16)
print(int16('12253'))