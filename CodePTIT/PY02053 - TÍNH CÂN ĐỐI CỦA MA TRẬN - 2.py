n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
k=int(input())
up = 0
down = 0
for i in range(len(a)):
    for j in range(len(a)):
        if i+j<n-1:
            down += a[i][j]
        elif i+j>n-1:
            up += a[i][j]
tmp = abs(down - up)
print('YES' if tmp <= k else 'NO')
print(tmp)
