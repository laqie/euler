# def phi(n):
#     return filter(lambda x: n % x != 0, xrange(1, n))

# print max(map(lambda n: n / phi(n), xrange(1000000)))

# m = 0
# for n in xrange(1000000):
#     p = float(phi(n))
#     if n == 6:
#         print n / p
#     if n / p > m:
#         m = n / p
#         print n

# print phi(6)

# answer: