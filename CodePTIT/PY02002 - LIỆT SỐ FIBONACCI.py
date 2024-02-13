arr=[0,1]
for i in range(2,94):
    arr.append(arr[i-1]+arr[i-2])
for i in range(int(input())):
    start,end=map(int,input().split())
    for j in range(start,end+1):
        print(arr[j],end=" ")
    print()