def find(n,k):
    if k==2**(n-1): return n
    elif k>2**(n-1): return find(n-1,k-2**(n-1))
    return find(n-1,k)
for test in range(int(input())) :
    n, k = [int(x) for x in input().split()]
    print(chr(find(n,k)+ord('A')-1))
