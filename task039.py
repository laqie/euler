all_perimeters = [a + b + (a ** 2 + b ** 2) ** 0.5 for a in xrange(1, 250) for b in xrange(a + 1, 500)]

m, p = 0, 0
for i in xrange(1, 1001):
    c = all_perimeters.count(i)
    if c > m:
        m, p = c, i

print m, p

# print len(s)