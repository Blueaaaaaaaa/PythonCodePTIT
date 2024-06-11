while True:
    s = int(input())
    if s == -1:
        break
    print("YES" if s % 11 == 0 else "NO")