from primes import primes

# all_primes = primes(9999)

def factors(n):
    p = primes(n + 1)
    n = float(n)
    result = []
    while n > 1:
        for i in p:
            if n % i == 0:
                result.append(i)
                n /= i
    return set(result)

n, l, k = 61000, 4, 0
while True:
    if len(factors(n)) == l:
        k += 1
        # print n, k, factors(n)
    else:
        k = 0
    if k == l:
        print n - k + 1
        break
    elif k >= 2:
        print n, factors(n)
    n += 1