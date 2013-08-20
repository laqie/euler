p = 5
def get_sum(n, p):
    result = 0
    while n > 0:
        result += (n % 10) ** p
        n //= 10
    return result


checkp = lambda n: get_sum(n, p) == n
import time
s = time.time()
# print sum((n for n in xrange(2, p * 9 ** p) if get_sum(n, p) == n))
print sum(filter(checkp, xrange(2, p * 9 ** p)))
print time.time() - s

