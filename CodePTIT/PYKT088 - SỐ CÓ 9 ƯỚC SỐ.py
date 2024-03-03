from math import *
n=int(input())
num=int(sqrt(n))+1

def sieve():
    temp[0]=temp[1]=0
    for i in range(2,num+1):
        if temp[i]==0:
            continue
        primes.append(i)
        for j in range(i*i,num,i):
            temp[j]=0
primes=[]
temp = [1]*(num+1)
sieve()
temp=0
count=0
while True:
    if primes[temp]**8>n:
        break
    count+=1
    temp+=1
# print(count)
# print(primes)
for i in range(len(primes)):
    if primes[i]**4>n:
        break
    for j in range(i+1,len(primes)):
        if (primes[i]*primes[j])**2>n:
            break
        else: count+=1
print(count)