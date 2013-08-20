numbers = [n * (n + 1) / 2 for n in xrange(19)]
with open('words.txt') as f:
    print len(filter(lambda w: sum(map(lambda c: ord(c) - 64, w)) in numbers, map(lambda w: w.strip('"'), f.read().split(','))))

