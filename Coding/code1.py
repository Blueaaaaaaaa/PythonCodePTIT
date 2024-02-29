str="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def trans(n,m):
    s=""
    while n:
        s+=str[n%m]
        n//=m
    return s[::-1]
for test in range(int(input())):
    n,m=map(int,input().split())
    print(trans(n,m))
