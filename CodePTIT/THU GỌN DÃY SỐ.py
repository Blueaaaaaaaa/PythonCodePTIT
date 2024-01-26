test= int(input())
arr=[int(i) for i in input().split()]
res=[]
for i in arr:
    if len(res)==0:
        res+=[i]
    else:
        if (res[-1]+i)%2==0:
            res.pop()
        else: res+=[i]
print(len(res))