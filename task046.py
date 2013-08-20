def primes(n):
    sieve = [True] * n
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * (( n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]


def is_dsquare(n):
    r = (n / 2.) ** 0.5
    return r == int(r)

all_primes = primes(20000)

n = 33
found = False
while not found:
    n += 2
    for prime in all_primes:
        if prime > n:
            found = True
            break
        if prime == n or is_dsquare(n - prime):
            break


print n