from math import *
def sum(n):
    sum=0
    for i in range(len(n)):
        sum+=int(n[i])
    return sum
def product(n):
    if n=='0'*len(n):
        return 0
    product=1
    for i in range(len(n)):
        if int(n[i])!=0:
            product*=int(n[i])
    return product
for test in range(int(input())):
    ip=input()
    s=ip[::2]
    p=ip[1::2]
    print(sum(s),product(p))

