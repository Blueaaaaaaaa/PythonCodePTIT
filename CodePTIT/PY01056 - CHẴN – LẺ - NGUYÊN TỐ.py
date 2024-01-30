from math import *
def isprimes(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
def sum(n):
    sum=0
    for i in range(len(n)):
        sum+=int(n[i])
    return sum
def check(n):
    if not isprimes(sum(n)):
        return "NO"
    for i in range(len(n)):
        if i%2==0 and int(n[i])%2==1:
            return "NO"
        if i%2==1 and int(n[i])%2==0:
            return "NO"
    return "YES"
for test in range(int(input())):
    n=input()
    print(check(n))

