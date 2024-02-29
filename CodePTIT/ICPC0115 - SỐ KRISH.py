from math import *
for test in range(int(input())):
    n=input()
    sum=0
    for i in range(len(n)):
        sum+=factorial(int(n[i]))
    print("Yes" if sum==int(n) else "No")