def period(n):
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    if n == 1:
        return 0
    m = 10 % n
    result = 1
    while m > 1:
        m = m*10 % n
        result += 1
    return result

import time

s = time.time()
# m = 1
# n = 0

for x in xrange(1000, 1, -1):
    p = period(x)
    if p == x or p == x - 1:
        print p, x
        break
    # if p > m:
    #     m, n = p, x
    # m = p if p > m else m

e = time.time()
# print m, n

print "Elapsed time: ", e - s


