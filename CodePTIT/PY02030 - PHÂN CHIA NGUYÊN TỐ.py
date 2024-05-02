from math import *
def primes(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return n>1

n=int(input())
a=map(int,input().split())
b,dict,ans=[],{},False
for i in a:
    if i not in dict:
        b.append(i)
        dict[i]=1
for i in range(len(b)):
    if primes(sum(b[:i+1])) and primes(sum(b[i+1:])):
        ans=True
        print(i)
        break
if ans==False: print("NOT FOUND")
