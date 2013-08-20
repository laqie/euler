with open("triangle.txt") as f:
    data = map(lambda x: map(int, x), map(lambda s: s.split(), f.readlines()))


def findpath(data):
    for i in xrange(1, len(data)):
        for j in xrange(len(data[i])):
            data[i][j] += data[i - 1][j] if j == 0 else data[i - 1][j - 1] if j == len(data[i]) - 1 else max(data[i - 1][j], data[i - 1][j - 1])
    return max(data[-1])


print findpath(data)
  