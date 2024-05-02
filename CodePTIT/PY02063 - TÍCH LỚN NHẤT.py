n=int(input())
a = sorted([int(x) for x in input().split()])
res=[]
res = []
res.append(a[0] * a[1])
res.append(a[0] * a[1] * a[n - 1])
res.append(a[n - 3] * a[n - 2] * a[n - 1])
res.append(a[n - 2] * a[n - 1])
print(max(res))