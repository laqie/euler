for a in xrange(1, 1000):
    for b in xrange(a, 1000):
        c = 1000 - a - b
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            print a, b, c
            print a * b * c
  