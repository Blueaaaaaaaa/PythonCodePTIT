import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def side_length(self, point1, point2):
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

    def is_valid_triangle(self):
        a = self.side_length(self.p1, self.p2)
        b = self.side_length(self.p2, self.p3)
        c = self.side_length(self.p3, self.p1)
        return (a + b > c) and (a + c > b) and (b + c > a)

    def perimeter(self):
        if not self.is_valid_triangle():
            return "INVALID"
        a = self.side_length(self.p1, self.p2)
        b = self.side_length(self.p2, self.p3)
        c = self.side_length(self.p3, self.p1)
        return round(a + b + c, 3)

def main():
    n = int(input().strip())
    results = []
    for _ in range(n):
        x1, y1, x2, y2, x3, y3 = map(float, input().strip().split())
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)
        triangle = Triangle(p1, p2, p3)
        result = triangle.perimeter()
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
