i=1
j=2
num =[]
even=[]
num.append(i)
num.append(j)
k = i+j
while k < 4000000:
    num.append(k)
    i = j
    j = k
    k = i+j
for i,val in enumerate(num):
    if val%2 == 0:
        even.append(val)

print sum(even)
