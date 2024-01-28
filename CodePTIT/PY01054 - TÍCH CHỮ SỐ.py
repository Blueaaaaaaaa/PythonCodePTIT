def isum(n):
    sum=1
    for i in range(len(n)):
        if int(n[i])!=0:
            sum*=int(n[i])
    return sum

for test in range(int(input())):
    n=input()
    print(isum(n))

