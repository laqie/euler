from time import time

s = time()

MAX = 500000
sieve = [0] * MAX

for i in xrange(2, MAX):
    if sieve[i] == 0:
        for j in xrange(2 * i, MAX, i):
            sieve[j] += 1
    if sieve[i + 3] == 4 \
        and sieve[i + 2] == 4 \
        and sieve[i + 1] == 4 \
        and sieve[i] == 4:
        print i
        break

print 'Elapsed time:', time() - s