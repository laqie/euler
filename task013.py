with open('numbers') as f:
    print str(sum([int(x) for x in f.readlines()]))[:10]