a, b, i, d = 1, 1, 1, 10 ** 999
while a % d == a:
    a, b, i = b, a + b, i + 1
print i

  