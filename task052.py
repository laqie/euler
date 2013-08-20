def check(n):
    s = set(str(n))
    for x in xrange(2, 7):
        if set(str(x * n)) != s:
            return False
    return True


n = 1
while True:
    if check(n):
        print n
        break
    n += 1