for test in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=False
    for i in a:
        if a.count(i)>(n//2):
            print(i)
            ans=True
            break
    if ans==False: print("NO")