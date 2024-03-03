for test in range(int(input())):
    s=input()
    if s[-1:]=='6' and s[-2:-1]=='8':
        print("YES")
    else: print("NO")