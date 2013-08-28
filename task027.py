def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in xrange(2, int(abs(num)**0.5 + 2)):
        if num % x == 0:
            return False
    else:
        return True

def get_length(a, b):
    f = lambda n: n ** 2 + a*n + b
    n, length = 0, 0
    while is_prime(f(n)):
        n += 1
    return n

A, B, m = 0, 0, 0
for a in xrange(-999, 1000, 2):
    for b in xrange(abs(a), 1000):
        if not is_prime(b):
            continue
        c = get_length(a, b)
        if c > m:
            m, A, B = c, a, b
        m = max(m, c)


print m, A, B, A * B
