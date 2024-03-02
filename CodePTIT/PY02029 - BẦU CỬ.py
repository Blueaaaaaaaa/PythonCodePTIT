n,m=map(int,input().split())
a=[int(i) for i in input().split()]
dict,maxn,ans,res={},0,0,0
for i in a:
    if i not in dict:
        dict[i]=1
    else: dict[i]+=1
    maxn=max(maxn,dict[i])
for i in range(1,m+1):
    if dict[i]!=maxn and dict[i]>res:
        res=dict[i]
        ans=i
print(ans if ans else "NONE")
        