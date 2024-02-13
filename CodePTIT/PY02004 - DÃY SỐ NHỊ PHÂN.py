n=int(input())
arr=[int(x) for x in input().split()]
cnt=0
for i in range(len(arr)-1):

    if arr[i]!=arr[i+1]:
        cnt+=1
        #print(arr[i], end=" ")
#if arr[-1:]!=arr[-1:-2]: cnt+=1
print(cnt)