import math
n,k=map(int,input().split())
start=10**(k-1)
end=10**k-1
cnt=0
for i in range(start,end,1):
    if math.gcd(i,n)==1:
        cnt+=1
        if cnt<10:
            print(i,end=" ")
        else:
            print(i)
            cnt=0
