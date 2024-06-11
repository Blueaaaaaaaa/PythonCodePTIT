arr = input().split()
maxn,ans = 0,""
for i in arr:
    if len(i) > maxn:
        maxn = len(i)
        ans = i
print(ans,len(ans))  