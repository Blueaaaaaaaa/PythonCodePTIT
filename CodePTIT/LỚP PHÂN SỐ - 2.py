import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rut_gon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def cong(self, other):
        tu_moi = self.tu * other.mau + other.tu * self.mau
        mau_moi = self.mau * other.mau
        ket_qua = PhanSo(tu_moi, mau_moi)
        ket_qua.rut_gon()
        return ket_qua

    def __str__(self):
        return f'{self.tu}/{self.mau}'

if __name__ == '__main__':
    tu_p, mau_p, tu_q, mau_q = map(int, input().split())
    p = PhanSo(tu_p, mau_p)
    q = PhanSo(tu_q, mau_q)
    tong = p.cong(q)
    print(tong)