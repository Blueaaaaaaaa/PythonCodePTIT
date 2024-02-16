from math import *
def isprimes(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
def check(n):
    for i in range(len(n)):
        if isprimes(int(n[i])) and not isprimes(i):
            return "NO"
        if not isprimes(int(n[i])) and isprimes(i):
            return "NO"
    return "YES"
for test in range(int(input())):
    n=input()
    print(check(n))

