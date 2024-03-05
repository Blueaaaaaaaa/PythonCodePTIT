from math import *
def primes(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
n,m=map(int,input().split())
a=[[int(i) for i in input().split()] for i in range(n)]
maxn=-1
ans={}
for i in range(n):
    for j in range(m):
        if primes(a[i][j]) and a[i][j]>maxn:
            maxn=a[i][j]
for i in range(n):
    for j in range(m):
        if a[i][j]==maxn:
            ans[i]=j
if maxn==-1: print("NOT FOUND")
else: 
    print(maxn)
    for i in ans:
        print('Vi tri [{}][{}]'.format(i,ans[i]))
