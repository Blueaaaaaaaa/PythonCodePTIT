for test in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=a[k:]+a[:k]
    for i in b:
        print(i,end=" ")
    print()