import time
from itertools import permutations
def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in xrange(2, int(num**0.5) + 2):
        if num % x == 0:
            return False
    else:
        return True

s = time.time()

print max(filter(is_prime, map(lambda x: int(''.join(x)), permutations('1234567', 7))))
# print filter(is_good, xrange(900000000, 987654322))
e = time.time()

print 'Elapsed time: ', e - s