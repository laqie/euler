from math import factorial as f

print sum(n for n in xrange(3, 50000) if sum(f(int(l)) for l in str(n)) == n)


