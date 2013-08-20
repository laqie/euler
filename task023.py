import time
s = time.time()
sum_factors = lambda n: sum(set(filter(lambda x: x < n, (reduce(list.__add__,
                    ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))))

max_int = 28123
result = 0
abdunants = set()

for n in xrange(1, max_int):
    if sum_factors(n) > n:
        abdunants.add(n)
    result += n if not any(n - a in abdunants for a in abdunants) else 0

print result

print 'Elapsed time: ', time.time() - s