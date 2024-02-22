from math import *
n=int(input())
a=[input() for j in range(n)]
b=[0]*n
count=0
for i in a:
    ans=0
    for j in range(n):
        if i[j] == 'C':
            ans+=1
    if ans>=2:
        count+=comb(ans,2)
for i in range(n):
    for j in range(n):
        if a[j][i]=='C':
            b[i]+=1
for i in b:
    if i>=2:
        count+=comb(i,2)
print(count)