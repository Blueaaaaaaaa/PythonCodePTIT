def sumof(s):
    sum=0
    for i in range(len(s)):
        sum+=ord(s[i])-ord('0')
    return str(sum)
n=input()
count=0
while len(n)>1:
    count+=1
    n=sumof(n)
print(count)