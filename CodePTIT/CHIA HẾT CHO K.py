a,k,n=map(int,input().split())
start=k-(a%k)
end=n-a
arr=[]
while start<=end:
    arr.append(str(start))
    start+=k
if len(arr)==0: print(-1)
else: print(' '.join(arr))