import math
for test in range(int(input())):
    ori=input()
    rev=ori[::-1]
    if math.gcd(int(ori),int(rev)) == 1:
        print("YES")
    else: print("NO")