def check(s):
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            return "NO"
    else: return "YES"

for i in range(int(input())):
    s=input()
    print(check(s))
