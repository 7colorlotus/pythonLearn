
L=list(range(1,11))
print(L)

L1=[x*x for x in range(1,11)]
print(L1)

L2=[x*x for x in range(1,11) if x%2==0]
print(L2)

L3=[m+n for m in 'abc' for n in 'ABC']
print(L3)

import os
print([d for d in os.listdir('.')])


L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s,str)])




