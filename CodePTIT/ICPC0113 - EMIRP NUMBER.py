def sieve(a):
    for i in range(2,1001):
        if a[i]:
            for j in range(i*i,100001,i):
                a[j]=0
for test in range(int(input())):
    n=int(input())
    a = [1] * 100001
    a[0] = a[1] = 0
    sieve(a)
    for i in range(n):
        ori=str(i)
        rev=ori[::-1]
        if (ori!=rev and int(rev)<=n) and (a[int(ori)]==1 and a[int(rev)]==1):
            print(ori,rev,end=" ")
            a[int(ori)] = 0
            a[int(rev)] = 0
    print()

