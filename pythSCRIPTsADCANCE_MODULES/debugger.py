a = [1, 2, 3]
b = [1, 2, 3]
c = 9
print(a + b)
'''
using python debugger
'''
import pdb
res1 = a + b
pdb.set_trace()
print(a + c)