from primes import primes

all_primes = primes(1000000)
up = 550
limit = 1000000

for l in xrange(up, 2, -1):
    i = 0
    while True:
        s = sum(all_primes[i:i + l])
        if s > limit:
            break
        if s in all_primes:
            print s, l
            exit(0)
        i += 1
