ip=input()
a,se=[],set()
length=(len(ip)//2)*2
for i in range(0,length,2):
    a.append(ip[i:i+2])
se={int(x) for x in a}
print(*sorted(se))