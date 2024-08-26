n, k = map(int, input().split())
def count_sets(n, k):
    if k == 0:
        return 1 if n == 0 else 0
    if n <= 0:
        return 0
    return (count_sets(n - k, k - 1) + count_sets(n, k - 1)) % (10**9 + 7)
print(count_sets(n, k))
