for test in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    dict={}
    for i in a:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for i in dict:
        if dict[i]%2==1:
            print(i)
            break