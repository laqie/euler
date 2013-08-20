import time
factors = lambda n: reduce(lambda x, y: x + y, (2 for i in xrange(1, int(n ** 0.5) + 1) if n % i == 0), 0)
tri = lambda x: x * (x + 1) / 2
 
 
start = time.time()
 
n = 1
while factors(tri(n)) < 500:
    n += 1
print tri(n)
 
end = time.time()
 
print "Elapsed time: ", end - start