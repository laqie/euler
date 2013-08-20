def check(n):
    for x in xrange(1, 21):
        if not n % x == 0:
            return False
    return True

n = 20
while not check(n):
    n += 20

print n