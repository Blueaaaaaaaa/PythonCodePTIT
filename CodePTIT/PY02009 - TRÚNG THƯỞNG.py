for i in range(int(input())):
    n=int(input())
    a=[0]*1001
    cnt=0
    while True:
        num=int(input())
        a[num]+=1
        cnt+=1
        if cnt==n: break
    ans=0
    op=0
    for i in range(1000,0,-1):
        if a[i]>=ans:
            ans=a[i]
            op=i
    print(op)