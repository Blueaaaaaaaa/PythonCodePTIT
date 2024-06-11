n = int(input())
arr = []
for i in range(n): arr.append(input())
res,tmp = [] , []
for i in range(n):
    # print(i,arr[i])
    if len(arr[i]): tmp.append(arr[i])
    else:
        res.append(tmp)
        tmp = []
if len(tmp) : res.append(tmp)
for _ in res:
    print(_[0],len(_)-1,sep=': ')