for test in range(int(input())):
    s=input()+'z'
    res=""
    maxn=0
    for i in range(len(s)):
        if '0'<=s[i]<='9':
            res+=s[i]
        elif len(res)>0:
            maxn=max(maxn,int(res))
            res=""

    print(maxn)
