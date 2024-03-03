n=int(input())
origin=[]
while True:
    res=[int(x) for x in input().split()]
    origin+=res
    if len(origin)==n:
        break
odd=[x for x in origin if x%2==1]
even=[x for x in origin if x%2==0]
odd=sorted(odd,reverse=True)
even=sorted(even,reverse=False)
ev,od=0,0
for i in range(n):
    if origin[i]%2==0:
        print(even[ev],end=" ")
        ev+=1
    else:
        print(odd[od],end=" ")
        od+=1
