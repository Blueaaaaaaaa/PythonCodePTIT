class TransposeMatrix:
    def __init__(self, matrix, n, m):
        self.matrix = matrix
        self.n = n
        self.m = m
    
    def transpose(self):
        _new = [[0] * self.n for _ in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                _new[j][i] = self.matrix[i][j]
        return _new

def main():
    num_tests = int(input().strip())
    for _ in range(num_tests):
        n, m = map(int, input().strip().split())
        _matrix = []
        for i in range(n):
            _matrix.append(list(map(int, input().strip().split())))
        result = TransposeMatrix(_matrix, n, m).transpose()
        for row in result:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
