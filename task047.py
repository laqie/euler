from factors import factor
from time import time

s = time()
n, l, k = 2, 4, 0
while True:
    if len(set(factor(n))) == l:
        k += 1
    else:
        k = 0
    if k == l:
        print n - k + 1
        break
    n += 1

print 'Elapsed time:', time() - s