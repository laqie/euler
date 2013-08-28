from math import factorial
from time import time

s = time()
f = [factorial(x) for x in xrange(10)]
print sum(n for n in xrange(3, f[9] * 7) if sum(f[int(l)] for l in str(n)) == n)
print 'Elapsed time:', time() - s


