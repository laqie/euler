i = 2
n = 600851475143
while i * i <= n:
    if i * i == n:
        n = i
        break

    while n%i == 0:
        n /= i
    i += 1

print (n)

  