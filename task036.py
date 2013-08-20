is_palindrom = lambda s: s == s[::-1]
print sum(filter(lambda n: is_palindrom(str(n)) and is_palindrom(bin(n)[2:]), xrange(1, 1000000, 2)))

