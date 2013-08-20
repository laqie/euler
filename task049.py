def primes(n):
    sieve = [True] * n
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * (( n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]


all_primes = filter(lambda n: n > 1487, primes(9999))

for a in all_primes:
    for b in all_primes[all_primes.index(a) + 1:]:
        if set(str(a)) == set(str(b)):
            c = b + b - a
            if c > 9999:
                break
            if set(str(b)) == set(str(c)) and b + b - a in all_primes:
                print "%d%d%d" % (a, b, c)
                exit(0)
