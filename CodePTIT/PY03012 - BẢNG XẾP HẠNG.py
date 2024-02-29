data,a=[],[]
for i in range(int(input())):
    name=input()
    correct,submit=map(int,input().split())
    a=[name,correct,submit]
    data.append(a)
data.sort(key=lambda x: (-x[1],x[2],x[0]))
for i in data:
    print(*i)