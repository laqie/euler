from math import sqrt

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in xrange(2, int(sqrt(num) + 2)):
        if num % x == 0:
            return False
    else:
        return True

n = 1
p = 3
while True:
    if is_prime(p):
        n += 1
    if n == 10001:
        print p
        break
    p += 2