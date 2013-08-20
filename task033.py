from fractions import Fraction

def check((n, d)):
    a, b = n // 10, n % 10
    a1, b1 = d // 10, d % 10
    f = Fraction(n, d)
    if (a == b1 and a1 != 0 and Fraction(b, a1) == f)\
        or (b == a1 and b1 != 0 and Fraction(a, b1) == f):
        return True
    return False

print reduce(lambda n, x: n * Fraction(*x),
             filter(check, ((n, d) for n in xrange(10, 100) for d in xrange(n, 100) if n % 10 != 0 and d != n)), Fraction(1, 1)).denominator

