divisors_sum = lambda n: sum(set(filter(lambda x: x < n, (reduce(list.__add__,
                    ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))))

N = 10000
# print reduce(lambda r, (x, y): r + x,
#              filter(lambda (x, y): y > 1 and not x == y and divisors_sum(y) == x,
#                     map(lambda x: (x, divisors_sum(x)), xrange(1, N + 1))), 0)

result = 0
for n in xrange(1, 10000):
    m = divisors_sum(n)
    if 1 < m != n and divisors_sum(m) == n:
        result += n

print result

