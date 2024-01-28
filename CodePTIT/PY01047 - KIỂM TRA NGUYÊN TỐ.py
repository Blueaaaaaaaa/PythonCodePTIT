from math import *
def check(n):
    if n<2: return "NO"
    for i in range(2,int(sqrt(n))):
        if n % i == 0:
            return "NO"
    return "YES"
for test in range(int(input())):
    ip=input()
    n=ip[-4:]
    print(check(int(n)))


