from math import *
while True:
    a=[int(x) for x in input().split()]
    if a==[0,0,0,0]:
        break
    cnt=0
    while a.count(a[0])!=4:
        cnt+=1
        p = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - p)
    print(cnt)