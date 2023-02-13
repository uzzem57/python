a = [1,2,3,4,1,2,4,6,6,6]
s = 0
for i in range(len(a) - 1):
    s += a[i + 1:].count(a[i])
print(s)





