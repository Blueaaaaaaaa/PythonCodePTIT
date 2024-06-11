while True:
    s = input()
    if s == "-1":
        break
    n = int(s)
    k = (9-n%9)%9
    print(n+(9-n%9)%9)