ss="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    ip=input()
    if ip=='0':
        break
    k,s=ip.split()
    res=''
    for i in s:
        id=ss.find(i)
        res+= ss[(id+int(k))%28]
    print(res[::-1])