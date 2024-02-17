a=[1]*100001
a[0]=a[1]=0
for i in range(2,1001):
    if a[i]:
        for j in range(i*i,100001,i):
            a[j]=0
for test in range(int(input())):
    count=0
    for i in range(int(input())-5):
        if a[i] and a[i+6]:
            if a[i+2] or a[i+4]:
                count+=1
    print(count)