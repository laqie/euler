def path(n):
    result = [1]
    while len(result) != n:
        result = [sum(result[:i + 1]) for i in xrange(len(result))]
        result.append(result[-1] * 2)
    return sum(result) * 2

print path(20)
