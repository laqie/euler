def collatz(n):
    result = 1
    while not n == 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        result += 1
    return result


m = 0
z = 0
import time

start = time.time()
for i in xrange(1000000, 3, -1):
    c = collatz(i)
    if c > m:
        m = c
        z = i

end = time.time()
print z

print 'Elapsed time: ', end - start




  