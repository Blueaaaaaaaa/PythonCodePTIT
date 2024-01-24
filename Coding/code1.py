for test in range(int(input())):
    arr=map(list(int,input().split()))
    for i in range(1,len(arr)):
        if (arr[i]+arr[i-1])%2==0:
            del arr[i-1]: