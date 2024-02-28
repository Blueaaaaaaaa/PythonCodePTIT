for test in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a=sorted(a)
    L,R=a[0],a[-1]
    arr=[int(x) for x in range(L,R+1)]
    count=0
    for i in arr:
        if i not in a:
            count+=1
    print(count)