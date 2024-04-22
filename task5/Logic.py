class Logic:
    @staticmethod
    def shift_row_right(array, row_index):
        row = array[row_index]
        first_elem = row[0]
        row[0] = row[3]
        row[3] = row[2]
        row[2] = row[1]
        row[1] = first_elem

    @staticmethod
    def shift_row_left(array, row_index):
        row = array[row_index]
        first_elem = row[0]
        row[0] = row[1]
        row[1] = row[2]
        row[2] = row[3]
        row[3] = first_elem

    @staticmethod
    def shift_col_down(array, col_index):
        zipped_rows = zip(*array)
        transposed_matrix = [list(row) for row in zipped_rows]
        Logic.shift_row_right(transposed_matrix, col_index)
        unzipped_rows = zip(*transposed_matrix)
        array[:] = [list(row) for row in unzipped_rows]

    @staticmethod
    def shift_col_up(array, col_index):
        zipped_rows = zip(*array)
        transposed_matrix = [list(row) for row in zipped_rows]
        Logic.shift_row_left(transposed_matrix, col_index)
        unzipped_rows = zip(*transposed_matrix)
        array[:] = [list(row) for row in unzipped_rows]
