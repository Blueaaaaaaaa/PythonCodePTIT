for test in range(int(input())):
    n,m,k=list(map(int,input().split()))
    a1=[int(i) for i in input().split()]
    a2=[int(i) for i in input().split()]
    a3=[int(i) for i in input().split()]
    ans,t1,t2,t3=0,0,0,0
    while t1<n and t2<m and t3<k:
        if a1[t1]==a2[t2] and a1[t1]==a3[t3]:
            print(a1[t1],end=" ")
            ans=1
            t1+=1
            t2+=1
            t3+=1
        elif a1[t1]<a2[t2]: t1+=1
        elif a2[t2]<a3[t3]: t2+=1
        elif a3[t3]<a1[t1]: t3+=1
    if ans==0: print("NO")
    else: print()