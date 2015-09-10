num = []
sums = 0
for i in xrange(1000):
            
    if i%3 == 0:
         num.append(i)
    elif i%5 == 0:
        num.append(i)
sums = sum(num)
print sums
print num
