tmp=[0]*1001
primes=[]
def sieve():
    for i in range(2,1001):
        if tmp[i]==0:
            primes.append(i)
        for j in range(i*i,1001,i):
            tmp[j]=1
sieve()
n=int(input())
a=[int(x) for x in input().split()]
res=[]
for i in a:
    if i in primes:
        res.append(i)
res=sorted(res)
temp=0
for i in a:
    if i not in primes:
        print(i,end=" ")
    else:
        print(res[temp],end=" ")
        temp+=1
