ip=input()
a,dict=[],{}
length=(len(ip)//2)*2
for i in range(0,length,2):
    a.append(ip[i:i+2])
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(*dict)