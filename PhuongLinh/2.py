n, k = map(int, input().split())
if k > n:
    print(0)
else:
    if k == 0 or k == n:
        print(1)
    else:
        k = min(k, n - k)
        num = 1
        den = 1
        for i in range(k):
            num = (num * (n - i)) % (10**9 + 7)
            den = (den * (i + 1)) % (10**9 + 7)
        result = (num * pow(den, 10**9 + 5, 10**9 + 7)) % (10**9 + 7)
        print(result)
