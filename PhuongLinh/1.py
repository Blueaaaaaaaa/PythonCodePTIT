n, k = map(int, input().split())
result = 1
for i in range(k):
    result *= (n - i)
    result %= (10**9 + 7)
print(result)
