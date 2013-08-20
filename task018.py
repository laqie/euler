with open("task018") as f:
    data = map(lambda x: map(int, x), map(lambda s: s.split(), f.readlines()))


def findpath(data):
    for i, row in enumerate(data[1:], 1):
        for j in xrange(len(row)):
            data[i][j] += data[i - 1][j] if j == 0 else data[i - 1][j - 1] if j == len(row) - 1 else max(data[i - 1][j], data[i - 1][j - 1])
    return max(data[-1])


print findpath(data)