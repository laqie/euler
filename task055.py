def reverse(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

k = 0
for i in xrange(10000):
    for x in xrange(50):
        i += reverse(i)
        if is_palindrome(i):
            break
        if x == 49:
            k += 1
print k
