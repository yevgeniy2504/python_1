class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join([" ".join([str(j) for j in i]) for i in self.matrix])

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Матрицы должны иметь одинаковую размерность')
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError('Number of columns in the first matrix must match the number of rows in the second matrix')
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                sum_ = 0
                for k in range(len(other.matrix)):
                    sum_ += self.matrix[i][k] * other.matrix[k][j]
                row.append(sum_)
            result.append(row)
        return Matrix(result)


m1 = Matrix([[1, 2, 5],
             [3, 4, 7],
             [5, 7, 1]])
m2 = Matrix([[5, 6, 8],
             [7, 8, 1],
             [6, 9, 1]])


if __name__ == '__main__':
    print(m1)
    print(m1 == m2)

    m3 = m1 + m2
    print(m3)

    m4 = m1 * m2
    print(m4)
