for test in range(int(input())):
    n=int(input())
    A=[int(x) for x in input().split()]
    B=[int(x) for x in input().split()]
    A.sort()
    B.sort()
    ans=0
    for i in range(n):
        if B[i]<A[i]:
            print("NO")
            ans=1
            break
    if ans=0: print("YES")
