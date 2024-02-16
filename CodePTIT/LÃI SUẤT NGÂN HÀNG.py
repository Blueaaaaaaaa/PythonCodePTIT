for i in range(int(input())):
    ori,inte,exp=map(float,input().split())
    k=0
    while ori < exp:
        ori*=(1+inte/100)
        k+=1
    print(k)
