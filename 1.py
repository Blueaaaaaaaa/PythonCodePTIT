class Point:
    def __init__(self):
        self.x = x
        self.y = y
    def requires(self):
        
    def valid(self):
        if self.x < 0 or self.y < 0 or self.z < 0:
            return False
        return True
if __name__ == "__main__":
    p = Point(1, 2, 3)
    print(p.valid())
    