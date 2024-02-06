ip=input()
n=len(ip)
check=[0]*n
def track(s,k):
    if k==n:
        print(s)
        return
    for i in range(n):
        if check[i]==0:
            check[i]=1
            track(s+ip[i],k+1)
            check[i]=0
track("",0)