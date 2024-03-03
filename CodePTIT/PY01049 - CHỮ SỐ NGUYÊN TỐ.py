from math import *
def isprimes(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return n>1
def check(n):
    if not isprimes(len(n)): return "NO"
    pri,nol=0,0
    for i in range(len(n)):
        if isprimes(int(n[i])):
            #print(n[i])
            pri+=1
        else: nol+=1
    #print(pri,nol)
    if pri>nol: return "YES"
    else: return "NO"

for test in range(int(input())):
    n=input()
    print(check(n))

