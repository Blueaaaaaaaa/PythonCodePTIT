n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    for j in range(1, 7):
        if i >= j:
            dp[i] = (dp[i] + dp[i - j]) % (10**9 + 7)
print(dp[n])
