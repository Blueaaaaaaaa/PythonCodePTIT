def check(n):
    if len(n)%2==0: return "NO"
    if n[0]==n[1] or n[0]!=n[len(n)-1]: return "NO"
    for i in range(2,len(n),2):
        if n[i]!=n[0]:
            return "NO"
    return "YES"
for test in range(int(input())):
    n=input()
    print(check(n))

