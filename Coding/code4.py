import math
class simplify():
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
    def tuu(self,inter):
        return (self.tu*inter.mau+self.mau+inter.tu)
    def mauu(self,inter):
        return self.mau*inter.mau
    def ans(self,inter):
        num=self.tuu(inter)
        den=self.mauu(inter)
        res=math.gcd(num,den)
        return f'{num//res}/{den//res}'
if __name__=='__main__':
    a,b,c,d=map(int,input().split())
    ps1=simplify(a,b)
    ps2=simplify(c,d)
    print(ps1.ans(ps2))