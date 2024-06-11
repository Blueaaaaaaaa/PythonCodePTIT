def check(n,h):
    count = 0
    for i in range(n):
        tmp = sum(int(x) for x in str(i))
        if tmp == h:
            count += 1
    return count
while True:
    s = input()
    if s == "-1":
        break
    n,h = map(int, s.split())
    print(check(n,h))
    