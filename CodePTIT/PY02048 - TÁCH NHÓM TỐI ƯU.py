n , k = map(int, input().split())
a = sorted(list(map(int, input().split())))
count = 1
for i in range(1,len(a)):
    if a[i] - a[i-1] > k:
        count += 1
print(count)