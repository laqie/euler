from itertools import permutations
from time import time

s = time()
DIVISORS = (17, 13, 11, 7, 5, 3, 2)
NUMBERS = set(xrange(10))

# cba = lambda x: reduce(lambda n, a: n*10 + a, x)

def cba(items):
    result = 0
    for i in items:
        result *= 10
        result += i
    return result

n = []
for divisor in DIVISORS:
    if not n:
        n = filter(lambda n: cba(n) % divisor == 0, permutations(NUMBERS, 3))
    else:
        tmp = []
        for item in n:
            for i in NUMBERS - set(item):
                if cba((i, ) + item[:2]) % divisor == 0:
                    tmp.append((i, ) + item)
        n = tmp[::]

print sum(map(lambda x: cba(x), map(lambda x: tuple(NUMBERS - set(x)) + x, n)))


print 'Elapsed time:', time() - s