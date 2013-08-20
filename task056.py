m = 0
s = lambda num: reduce(lambda a, b: a + int(b), num, 0)

for i in xrange(1, 101):
    for j in xrange(1, 101):
        m = max(s(str(i ** j)), m)


print m

