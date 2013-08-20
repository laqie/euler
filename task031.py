lis = [1] + [0 for i in range(1,201)]
for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
   for j in range(coin, 201):
      lis[j] += lis[j - coin]
print lis[200]