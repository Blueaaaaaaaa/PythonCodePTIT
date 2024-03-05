n=int(input())
if n<10: print(n)
else:
    while n>=10:
        front=len(str(n))/=2
        #back=len(n)-front
        n=str(n)
        m=int(n[:front+1]+n[front+1:])
        print(m)
        m=str(m)
    