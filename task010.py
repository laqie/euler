from math import sqrt

def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    for x in xrange(2, int(sqrt(num) + 2)):
        if num % x == 0:
            return False
    else:
        return True

result = 0
for x in xrange(1, 2000000):
    if is_prime(x):
        result += x

print result
# print is_prime(2)

  