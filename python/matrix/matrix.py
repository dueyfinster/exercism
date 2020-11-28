class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        if "\n" in matrix_string:
            unproc_rows = matrix_string.split('\n')
            for row in unproc_rows:
                srow = list(map(int,row.split(' ')))
                self.matrix.append(srow)
        else:
            nums = list(map(int, matrix_string.split(' ')))
            row = []
            for num in nums:
                row.append(num)
            self.matrix.append(row)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        column = []
        for row in self.matrix:
            if row[index-1] is not None:
                column.append(row[index-1])
        return column
