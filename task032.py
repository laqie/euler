# def check(n, m):
#     s = "%d%d%d" % (n, m, n * m)
#     print s
#     if '0' in s:
#         return False
#     if len(s) != 9:
#         return False
#     if len(set(s)) == 9:
#         return True
#     return False
#
# result = set()
# for i in xrange(5000):
#     for j in xrange(i, 10000):
#         n = "%d%d%d" % (i, j, i * j)
#         if len(n) == 9 and '0' not in n and len(set(n)) == 9:
#             print i, 'x',  j, '=', i * j
#             result.add(i * j)
#
#
# # print check(39, 186)
#
# print sum(result)

from itertools import permutations

