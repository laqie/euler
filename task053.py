from math import factorial

def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

c = 0
for n in xrange(1, 101):
    for r in xrange(1, n):
        if combinations(n, r) > 1000000:
            c += 1

print c