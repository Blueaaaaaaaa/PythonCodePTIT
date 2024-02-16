MAX = pow(10,4)

def PhanTich_ThuaSo (n):
    res = {2:0}
    if n%2==0:
        while n%2==0:
            res[2] = res.get(2) + 1
            n/=2
    i = 3
    while i<=n:
        if n%i==0:
            res[i] = 0
            while n%i==0:
                res[i] = res.get(i) +1
                n/=i
        i+=2
    return res


def So_Uoc_So( Dict):
    res = 1
    for i in Dict.keys():
        res *= (Dict.get(i) + 1)

    return res

def Day_Phan_NguyenTo():
    res = {}    #List luu cac so Phan Nguyen To
    UocSo_max = 0
    for i in range(1, MAX):
        if So_Uoc_So(PhanTich_ThuaSo(i)) > UocSo_max:
            UocSo_max = So_Uoc_So(PhanTich_ThuaSo(i))
            res[i] = 1
        else:
            res[i] = 0
    return res

# print(Day_Phan_NguyenTo())
t = int(input())
while t>0:
    n = int(input())
    while Day_Phan_NguyenTo().get(n) ==0:
        n+=1
    print(n)


    t-=1