from itertools import permutations
from time import time

s = time()
divisors = (17, 13, 11, 7, 5, 3, 2)
numbers = set(xrange(10))

# cba = lambda x: reduce(lambda n, a: n*10 + a, x)
def cba(items):
    result = 0
    for i in items:
        result *= 10
        result += i
    return result

n = []
for divisor in divisors:
    if not n:
        n = filter(lambda n: cba(n) % divisor == 0, permutations(numbers, 3))
    else:
        tmp = []
        for item in n:
            for i in numbers - set(item):
                if cba((i, ) + item[:2]) % divisor == 0:
                    tmp.append((i, ) + item)
        n = tmp[::]

print sum(map(lambda x: cba(x), map(lambda x: tuple(numbers - set(x)) + x, n)))


############# BAD
# print cba(1, *(5, 2, 3))


# def f(d, n = None, r = None, s = 0):
#     dv = divisors[d]
#     if d == len(divisors):
#         return n
#     if not n:
#         n = filter(lambda n: n % dv == 0 and len(set(abc(n))) == 3, xrange(0, 1000))
#         for item in n:
#             return f(d + 1, n)
#     else:
#         for item in n:
#             k = n
#             abcd = abc(item)
#             good, bad = abcd[:2], set(abcd[2:])
#             for i  in good:
#                 if cba([i] + good) % dv == 0:
#                     k.append()
#
#     return sum(n)
    # return f(d + 1, n)

# print f(0)
# n = 41314




# print cba(*abc(3145))
# while n > 0:
#     print n % 10
#     n //= 10

# abc = lambda n: (n // 100, n // 10 % 10, n % 10)
# cba = lambda a, b, c: a * 100 + b * 10 + c
#
#
# d17 = filter(lambda n: n % 17 == 0 and len(set(abc(n))) == 3, xrange(0, 1000))

# def check(n):
#     for i, d in enumerate(divisors):
#          if n // 10 ** i % 1000 % d != 0:
#              return False
#     return True


# result = 0
# for n in d17:
#     d8, d9, d10 = abc(n)
#     for d7 in numbers - {d8, d9, d10}:
#         if cba(d7, d8, d9) % 13 == 0:
#             for d1, d2, d3, d4, d5, d6 in permutations(numbers - {d7, d8, d9, d10}, 6):
#                 if cba(d6, d7, d8) % 11 == 0\
#                     and cba(d5, d6, d7) % 7 == 0\
#                     and cba(d4, d5, d6) % 5 == 0\
#                     and cba(d3, d4, d5) % 3 == 0\
#                     and cba(d2, d3, d4) % 2 == 0:
#                     l = reduce(lambda r, n: r*10 + n, [d1, d2 ,d3, d4, d5, d6, d7, d8, d9, d10], 0)
#                     result += l
# print result
print 'Elapsed time:', time() - s
