from time import time
from primes import is_prime

s = time()

n, primes = 3, 0
while True:
    primes += len(filter(is_prime,  (n  ** 2 - n + 1, (n - 1) ** 2 + 1, n ** 2 - 3 * n + 3)))
    if primes / (2. * n - 1) < 0.1:
        print n
        break
    n += 2

print 'Elapsed time:', time() - s

# 26241
# Elapsed time: 0.551295995712
