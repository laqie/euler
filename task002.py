a, b = 0, 1
result = a

while a < 4000000:
    a, b = b, a + b
    result += a if a % 2 == 0 else 0

print result
