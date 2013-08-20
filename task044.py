def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6.
    return n == int(n)

n = 1
pentagonal_numbers = []

while True:
    a = n * (3 * n - 1) / 2
    for b in pentagonal_numbers:
        if is_pentagonal(a - b) and is_pentagonal(a + b):
            print a - b
            exit(0)
    pentagonal_numbers.append(a)
    n += 1