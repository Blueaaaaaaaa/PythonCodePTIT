def town(n,start,temp,end):
    if n==1:
        print(start,"->",end)
    else:
        town(n-1,start,end,temp)
        print(start,"->",end)
        town(n-1,temp,start,end)
n=int(input())
town(n,"A","B","C")