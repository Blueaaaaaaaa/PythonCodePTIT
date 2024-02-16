from math import *
def primes(n,a):
    tmp=[]
    for i in range(2,n+1):
        if i not in tmp:
            a.append(i)
            for j in range(i*i,n+1,i):
                tmp.append(j)
a=[]
primes(1000,a)
ip=input().split()
for i in range(int(ip[0])):
    tmp=[int(x) for x in input().split()]
    for j in tmp:
        if j in a:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()