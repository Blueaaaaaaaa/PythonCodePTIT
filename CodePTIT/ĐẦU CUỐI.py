for i in range(int(input())):
    arr=list(int(i) for i in input())
    ans=1
    if len(arr)<4: ans=0
    if arr[0]==arr[-2] and arr[1]==arr[-1]:
        ans=1
    else: ans=0
    if(ans==0): print("NO")
    else: print("YES")