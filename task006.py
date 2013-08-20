n = 100
print pow(sum(xrange(n+1)), 2) - sum(map(lambda x: x*x, xrange(n+1)))
