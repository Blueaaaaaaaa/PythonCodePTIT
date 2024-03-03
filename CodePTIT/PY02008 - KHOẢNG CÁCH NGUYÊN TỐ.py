def primes(n,a):
    tmp=[]
    for i in range(2,n+1):
        if i not in tmp:
            a.append(i)
            for j in range(i*i,n+1,i):
                tmp.append(j)
a=[]
primes(10000,a)
n,x=map(int,input().split())
print(x,end=" ")
for i in range(n):
    x = x + a[i]
    print(x, end=" ")