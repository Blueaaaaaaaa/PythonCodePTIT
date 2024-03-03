for i in range(int(input())):
    a=list(int(i) for i in input())
    for i in range(len(a)-1,0,-1):
        if a[i]>=5:
            a[i-1]=a[i-1]+1
        a[i]=0
        if a[0]==10:
            a=[1]+a
            a[1]=0
    for x in a:
        print(x,end='')
    print()