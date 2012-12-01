class Matrix():

    def __init__(self, weight, arg = None):
        if isinstance(weight, list):
            self.weight = weight
        else:
            self.weight = [0] * weight
            for i in range(weight):
                self.weight[i] = [0] * arg

    def __getitem__(self, item):
        return self.weight[item]

    def __add__(self, matrix):
        result = Matrix(self.get_rows(), self.get_cols())
        for row in range(self.get_rows()):
            for col in range(self.get_cols()):
                result[row][col] = self.weight[row][col] + matrix[row][col]
        return result

    def __sub__(self, matrix):
        result = Matrix(self.get_rows(), self.get_cols())
        for row in range(self.get_rows()):
            for col in range(self.get_cols()):
                result[row][col] = self.weight[row][col] - matrix[row][col]
        return result

    def __mul__(vector_1, vector_2):
        result = Matrix(vector_1.get_rows(), vector_1.get_rows())
        for row in range(vector_1.get_rows()):
            for col in range(vector_1.get_rows()):
                result[row][col] = vector_1[col] * vector_2[row][0]
        return result

    def get_rows(self):
        return len(self.weight)

    def get_cols(self):
        return len(self.weight[0])


    def scalar_multiply(matrix, vector):
        result = []
        for k in range(matrix.get_cols()):
            product = 0
            for j in range(matrix.get_cols()):
                product += vector[j] * matrix[j][k]
            result.append(product > 0)
        return result

    @staticmethod
    def identity(size):
        identity = Matrix(size, size)
        for i in range(size):
            identity[i][i] = 1
        return identity

    def transpose(self):
        return map(lambda *vector: list(vector), *[self])