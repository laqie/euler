def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6.
    return n == int(n)


def is_hexagonal(x):
    n = (1 + (1 + 8 * x) ** 0.5) / 4.
    return n == int(n)

n = 286
while True:
    t = n * (n + 1) / 2
    if is_pentagonal(t) and is_hexagonal(t):
        print t
        break
    n += 1