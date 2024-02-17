def sumof(n):
    sum=0
    while n:
        sum+=n%10
        n//=10
    return sum
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a=sorted(a)
    a=sorted(a,key=sumof)
    for i in a:
        print(i,end=" ")
    print()