n,k=map(int,input().split())
arr=sorted(list({int(i) for i in input().split()}))
arr=[0]+arr
n=len(arr)
check=[0]*1001
def track(i):
    for j in range(check[i-1]+1,n-k+i):
        check[i]=j
        if i==k:
            for j in range(1,k+1):
                print(arr[check[j]],end=" ")
            print()
        else:
            track(i+1)
track(1)