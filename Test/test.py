n = 4
m = 5
triangle = []
for i in range(1):
    triangle.append([1]*(m))
for i in range(1, n):
    triangle.append([1] + [0]*m)
for i in range(1, n):
    for j in range(1, m):
        triangle[i][j] = triangle[i][j-1] + triangle[i-1][j]
for i in range(0, n):
    for j in range(0, m):
        print(triangle[i][j], end=" ")
    print()
