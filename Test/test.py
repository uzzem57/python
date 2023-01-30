a = int(input())
n = 0
summa = 1
n0 = 1
i = 0
while n <= a:
    summa = n
    n = n0 + n
    n0 = summa
    i += 1
    if a == n:
        print(i)
        break
if a < 0 or a != n:
    print(-1)
elif a == 0:
    print(0)





