def changed(n,b):
    s = '0123456789ABCDEF'
    ans=""
    while(n):
        ans+=s[n%b]
        n//=b
    return ans[::-1]
for test in range(int(input())):
    b = int(input())
    n = int(input(),2)
    print(changed(n,b))