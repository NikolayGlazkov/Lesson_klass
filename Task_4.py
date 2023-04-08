class Matrix:
    def __init__(self, data):
        self.data = data
        self.num_rows = len(data)
        self.num_cols = len(data[0])

    def __str__(self):
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.num_cols)]) for i in range(self.num_rows)])


matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = Matrix(matrix_data)
print(matrix)
