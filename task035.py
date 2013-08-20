def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


import time

s = time.time()
all_primes = set(primes(1000000))

def check(n):
    n = str(n)
    for _ in xrange(len(n) - 1):
        n = n[1:] + n[:1]
        if int(n) not in all_primes:
            return False
    return True

print len(filter(check, all_primes))

e = time.time()

print 'Elapsed time: ', e - s