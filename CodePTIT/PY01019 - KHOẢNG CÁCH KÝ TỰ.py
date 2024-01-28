def check(s1,s2):
    for i in range(1,len(s1)):
        d1 = abs(ord(s1[i]) - ord(s1[i - 1]))
        d2 = abs(ord(s2[i]) - ord(s2[i - 1]))
        if not d1==d2:
            return "NO"
    return "YES"
for test in range(int(input())):
    s1=input()
    s2=s1[::-1]
    print(check(s1,s2))
