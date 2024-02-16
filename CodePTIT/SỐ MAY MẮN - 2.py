for i in range(int(input())):
    ans = 1
    n = input()
    for i in range(len(n)):
        if n[i] != '4' and n[i] != '7':
            ans=0
    if(ans==1): print("YES")
    else: print("NO")