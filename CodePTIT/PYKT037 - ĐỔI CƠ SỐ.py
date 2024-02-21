s="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for test in range(int(input())):
    num,base=map(int,input().split())
    ans=""
    while num:
        ans+=s[num%base]
        num//=base
    print(ans[::-1])
