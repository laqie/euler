def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


all_primes = set(primes(1000000))

def get_items(n):
    result = [n]
    i = 1
    while i < len(str(n)):
        result += [n // 10 ** i, n % 10 ** i]
        i += 1
    return set(result)


# print t <= all_primes

r = []
for item in all_primes:
    if item < 10:
        continue
    if get_items(item) <= all_primes:
        r.append(item)
        if len(r) == 11:
            break

print r, len(r), sum(r)

  