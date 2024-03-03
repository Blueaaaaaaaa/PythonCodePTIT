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
arr=[int(i) for i in input().split()]
a=[]
myset=set()
for i in arr:
    if i not in myset:
        a.append(i)
        myset.add(i)
ans=False
for i in range(0,n):
    if sum(a[0:i+1]) in primes and sum(a[i+1:]) in primes:
        print(i)
        ans=True
        break
if ans==False: print("NOT FOUND")
                                                                                                                                                                                              