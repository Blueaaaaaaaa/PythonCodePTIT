def suma(n):
    sum=0
    while n:
        sum+=n%10
        sum//=10
    return sum
def ins(n):
    arr=[int(i) for i in str(n)]
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1])!=2:
            return False
    return True
for test in range(int(input())):
    n=int(input())
    if ins(n)==True and suma(n)%10==0:
        print("YES")
    else: print("NO")