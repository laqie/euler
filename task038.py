# def is_pandigital
p = lambda x, n: ''.join(map(lambda i: str(x * i), xrange(1, n + 1)))

def check(x, n):
    k = p(x, n)
    return len(k) == 9 and set(k) == set('123456789')


# z = lambda x, n: len(set(''.join(map(lambda i: str(x * i), xrange(1, n + 1))))) == 9
m = 0
for n in xrange(2, 4):
    for x in xrange(100000):
        if check(x, n):
            k = p(x, n)
            if k > m:
                m = k
            print x, n, k

print m