def rev(n):
    n=str(n)
    n=n[::-1]
    return int(n)
def check(n):
    for i in range(1000):
        if (n+rev(n))%7==0:
            return n+rev(n)
        else:
            n=n+rev(n)
    return -1
for test in range(int(input())):
    n=int(input())
    if n%7==0: print(n)
    else: print(check(n))