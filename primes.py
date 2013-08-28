import random

def primes(n):
    sieve = [True] * n
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * (( n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]


def rabin_miller_test(a, s, d, n):
    a = pow(a, d, n)

    if a == 1:
        return True

    for i in xrange(s - 1):
        if a == n - 1:
            return True
        a = (a * a) % n

    return a == n - 1


def is_prime(n):
    d, s = n - 1, 0

    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in xrange(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not rabin_miller_test(a, s, d, n):
            return False

    return True
  