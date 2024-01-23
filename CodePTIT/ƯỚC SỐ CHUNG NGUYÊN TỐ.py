import math
def isprimes(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
def sumof(n):
    sum=0
    while n:
        sum+=n%10
        n//=10
    return sum
for i in range(int(input())):
    a,b=map(int,input().split())
    c=math.gcd(a,b)
    if isprimes(sumof(c)): print("YES")
    else print("NO")