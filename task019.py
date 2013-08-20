from calendar import isleap
M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
W = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

N = 0
result = 0
mm = 0
for year in xrange(1900, 2001):
    for m_number in xrange(12):
        m = M[m_number]
        mm += 1
        if m_number == 1 and isleap(year):
            m += 1
        for d in xrange(1, m + 1):
            if N == 6 and d == 1 and not year == 1900:
                # print d, m_number + 1, year
                result += 1
            N = N + 1 if N < 6 else 0
            # print N

print result

