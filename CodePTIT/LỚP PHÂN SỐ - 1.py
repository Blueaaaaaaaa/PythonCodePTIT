import math
class simplify():
    def __init__(self,nume,deno):
        self.nume=nume
        self.deno=deno
    def ans(self):
        pro = math.gcd(self.nume, self.deno)
        return f'{self.nume//pro}/{self.deno//pro}'

if __name__=='__main__':
    n,m= map(int,input().split())
    point=simplify(n,m)
    print(point.ans())