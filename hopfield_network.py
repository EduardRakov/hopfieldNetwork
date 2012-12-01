from matrix import Matrix

class HopfieldNetwork():

    def __init__(self, size):
        self.weight = Matrix(size, size)

    def __getitem__(self, item):
        return self.weight[item]

    def train(self, vector):
        matrix_2 = Matrix(vector)
        matrix_1 = Matrix(matrix_2.transpose())
        matrix_3 = matrix_2 * matrix_1
        identity = Matrix.identity(len(vector))
        matrix_4 = matrix_3 - identity
        self.weight = self.weight + matrix_4

    def present(self, vector):
        result = Matrix.scalar_multiply(self.weight, vector)
        print(result)
        return result