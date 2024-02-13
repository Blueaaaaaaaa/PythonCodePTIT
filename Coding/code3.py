import math

class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,other):
        res=math.sqrt((self.x-other.x)**2+(self.y-other.y))
        return res
if __name__=="__main__":
    a,c,d,e,f,g=map(int,input().split())
