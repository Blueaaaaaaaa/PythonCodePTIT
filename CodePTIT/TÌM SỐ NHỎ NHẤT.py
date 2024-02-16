import math
for test in range(int(input())):
    s=input()
    res=""
    maxn=1e9
    for i in range(len(s)):
        if '0'<=s[i]<='9':
            res+=s[i]
        elif len(res)>0:
            maxn=min(maxn,int(res))
            res=""

    print(maxn)
