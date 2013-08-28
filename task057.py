from fractions import Fraction
from time import time

s = time()

def sqrt2(n):
    x = 1 + Fraction(1, 2)
    for _ in xrange(n):
        yield x
        x = 1 + Fraction(1, 1 + x)

def number_len(n):
    k = 0
    while n > 0:
        n //= 10
        k += 1
    return k

print len(filter(lambda x: len(str(x.numerator)) > len(str(x.denominator)), sqrt2(1000)))

print 'Elapsed time:', time() - s

# 153
# Elapsed time: 0.657220125198
