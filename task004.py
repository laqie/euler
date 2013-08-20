def is_palindrom(n):
    s = str(n)
    if s[0:len(s)/2] == s[len(s)/2:][::-1]:
        return True
    else:
        return False
maxi = 0
for i in xrange(999, 99, -1):
    for j in xrange(999, 99, -1):
        m = i*j
        if is_palindrom(m) and m > maxi:
            maxi = m

print is_palindrom(9009)
print maxi
