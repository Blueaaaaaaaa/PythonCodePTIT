from math import *
def isum(n):
    sum=0
    for i in range(len(n)):
        sum+=int(n[i])
    return sum
def isprimes(n):
    if n<2: return "NO"
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return "NO"
    return "YES"



for test in range(int(input())):
    n=input()
    if isum(n)%3==0:
        print("YES")
    else: print("NO")

