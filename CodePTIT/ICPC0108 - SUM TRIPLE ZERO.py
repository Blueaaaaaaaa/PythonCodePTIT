for test in range(int(input())):
    n=int(input())
    a=sorted(map(int,input().split()))
    count=0
    for i in range(n-2):
        start,end=i+1,n-1
        while start<end:
            tmp=a[i]+a[start]+a[end]
            if tmp==0:
                count+=1
                start+=1
            elif tmp<0:
                start+=1
            else:
                end-=1
    print(count)