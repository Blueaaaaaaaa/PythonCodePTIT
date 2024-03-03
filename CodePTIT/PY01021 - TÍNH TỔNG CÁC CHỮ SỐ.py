for test in range(int(input())):
    ip=input()
    str,num=[],[]
    for i in range(len(ip)):
        if ip[i] in '0123456789':
            num.append(int(ip[i]))
        else: str.append(ip[i])
    for x in sorted(str):
        print(x,end="")
    print(sum(num))