class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        lines = matrix_string.splitlines()
        for line in lines:
            row = list(map(int,line.split(' ')))
            self.matrix.append(row)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        column = []
        for row in self.matrix:
            if row[index-1] is not None:
                column.append(row[index-1])
        return column
