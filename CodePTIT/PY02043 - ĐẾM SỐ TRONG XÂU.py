for test in range(int(input())):
    n,m=input(),input()
    count=0
    N,M=len(n),len(m)
    #print(n,m)
    for i in range(N-M+1):
        if n[i:i+M]==m:
            #print(n[:i])
            #print(n[:i+1]+n[i+3:])
            n=n[:i]+n[i+3:]
            #print(m)
            count+=1
    print(count)