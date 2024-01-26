for t in range(int(input())):
    s = input()+'!'
    res=1
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            res+=1
        else:
            print(str(res)+s[i],end="")
            res=1
    print()