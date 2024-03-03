from math import *
def check(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))):
        if n % i == 0:
            return False
    return True
for test in range(int(input())):
    ip=input()
    sta=ip[-3:]
    end=ip[:3]
    if check(int(sta)) and check(int(end)):
        print("YES")
    else: print("NO")
