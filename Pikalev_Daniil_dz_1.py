class Matrix:

    def __init__(self, my_matrix):
        self.matrix = my_matrix

    def __str__(self):
        return f'Матрица:\n' + '\n'.join('\t'.join(map(str, line)) for line in self.matrix)

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range (len(self.matrix[0]))] for i in range (len(self.matrix))]
        return Matrix(result)


matrix_1 = [
    [1, 2],
    [3, 4],
    [5, 6],
]

matrix_2 = [
    [1, 2],
    [3, 4],
    [5, 6],
]

a = Matrix(matrix_1)
print(a)
b = Matrix(matrix_2)
print(b)
c = a + b
print(c)