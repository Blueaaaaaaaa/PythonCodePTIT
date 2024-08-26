n, m = map(int, input().split())
Y = list(map(int, input().split()))
result = 0
def count(m, n):
    if n < 0:
        return 0
    if m == 0:
        return 1 if n == 0 else 0
    result = 0
    for i in range(1, Y[m-1] + 1):
        result = (result + count(m - 1, n - i)) % (10**9 + 7)
    return result
print(count(m, n))
