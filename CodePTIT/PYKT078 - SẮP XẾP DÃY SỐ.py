for test in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    maxn=max(a)
    pos=-1
    for i in range(n):
        if a[i]==maxn:
            pos=i
            break
    a.insert(pos,m)
    negative,positive=[],[]
    for i in a:
        if i<0:
            negative.append(i)
        else: positive.append(i)
    print(*negative,*positive)