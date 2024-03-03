def isum(n):
    sum=0
    for i in range(len(n)):
        sum+=int(n[i])
    return sum
def check(n):
    s1=str(isum(n))
    s2=s1[::-1]
    if(len(s1))<2 or s1!=s2: return "NO"
    return "YES"

for test in range(int(input())):
    n=input()
    print(check(n))

