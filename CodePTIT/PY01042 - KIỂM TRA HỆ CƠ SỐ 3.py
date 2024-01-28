def check(ip):
    for i in range(len(ip)):
        if ip[i]!='0' and ip[i]!='1' and ip[i]!='2':
            return "NO"
    return "YES"
for test in range(int(input())):
    ip=input()
    print(check(ip))