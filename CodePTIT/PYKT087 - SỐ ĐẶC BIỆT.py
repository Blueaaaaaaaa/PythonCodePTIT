for testcase in range(int(input())):
    n,k = map(int,input().split())
    mod,ans,tmp = 10**9+7,0,1
    while k>0:
        if k&1 :
            ans = (ans % mod + tmp % mod)%mod
        k >>= 1
        tmp = (tmp % mod * n % mod)%mod
    print(ans % mod)