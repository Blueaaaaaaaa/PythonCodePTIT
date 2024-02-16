def valid(s):
    if len(s)%2==1 or s!=s[::-1]: return False
    for i in range(len(s)):
        if int(s[i])%2!=0:
            return False
    return True

for i in range(int(input())):
    s=int(input())
    for j in range(22,s,2):
        if valid(str(j)):
            print(j,end=' ')
    print()