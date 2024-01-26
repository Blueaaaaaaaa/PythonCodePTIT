import math
for test in range(int(input())):
    n=int(input())
    print(1, end=' ')
    for i in range(2,n//2+1):
        if n%i==0:
            cnt=0
            while n%i==0:
                n//=i
                cnt+=1
            print("* " + str(i) + "^" + str(cnt), end=" ")
    if n>1:
        print("* " + str(n) + "^1", end=" ")
    print()