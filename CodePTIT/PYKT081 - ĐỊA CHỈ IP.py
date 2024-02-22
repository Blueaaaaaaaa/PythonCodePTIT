for test in range(int(input())):
    arr=input().split('.')
    ans=True
    if len(arr)!=4: ans=False
    for i in arr:
        if not '0'<=i<='255':
            ans=False
    print("YES" if ans==True else "NO")